using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace ppd_lab5
{
    public class StateObject
    {
        // Client socket.  
        public Socket workSocket = null;
        // Size of receive buffer.  
        public const int BufferSize = 256;
        // Receive buffer.  
        public byte[] buffer = new byte[BufferSize];
        // Received data string.  
        public StringBuilder sb = new StringBuilder();

        public int i;
    }

    public class Program
    {
        private const int port = 80;

        // ManualResetEvent instances signal completion.  
        private static List<ManualResetEvent> connectDone = new List<ManualResetEvent>() { new ManualResetEvent(false) , new ManualResetEvent(false) , new ManualResetEvent(false) };
        private static List<ManualResetEvent> sendDone = new List<ManualResetEvent>() { new ManualResetEvent(false), new ManualResetEvent(false), new ManualResetEvent(false) };
        private static List<ManualResetEvent> receiveDone = new List<ManualResetEvent>() { new ManualResetEvent(false), new ManualResetEvent(false), new ManualResetEvent(false) };

        private static List<string> hostNames = new List<string>() { "cs.ubbcluj.ro", "cs.ubbcluj.ro", "cs.ubbcluj.ro" };

        private static List<String> response = new List<String>() { String.Empty, String.Empty, String.Empty };

        private static async void StartClient(string hostName, int i)
        {
            // Connect to a remote device.  
            try
            {
                // Establish the remote endpoint for the socket.  
                // The name of the   
                // remote device is "host.contoso.com".  
                IPHostEntry ipHostInfo = Dns.GetHostEntry(hostName);
                IPAddress ipAddress = ipHostInfo.AddressList[0];
                IPEndPoint remoteEP = new IPEndPoint(ipAddress, port);

                // Create a TCP/IP socket.  
                Socket client = new Socket(ipAddress.AddressFamily,
                    SocketType.Stream, ProtocolType.Tcp);

                StateObject s1 = new StateObject()
                {
                    workSocket = client,
                    i = i,
                };

                // Connect to the remote endpoint.  
                client.BeginConnect(remoteEP,
                    new AsyncCallback(ConnectCallback), s1);
                connectDone[i].WaitOne();

                // Send test data to the remote device.
                await Send(client, "GET / HTTP/1.1\r\nHost: "+hostName+"\r\nUser - Agent: Mozilla / 5.0(Windows NT 10.0; Win64; x64; rv: 56.0) Gecko / 20100101 Firefox / 56.0\r\nAccept: text / html,application / xhtml + xml,application / xml; q = 0.9,*/*;q=0.8\r\nAccept - Language: en-US,en;q=0.5\r\nAccept - Encoding: gzip, deflate\r\nReferer: http://clipart-library.com/clipart/575061.htm\r\nConnection: keep-alive\r\nUpgrade - Insecure-Requests: 1\r\nIf - Modified-Since: Wed, 01 Mar 2017 15:35:52 GMT\r\nIf - None-Match: \"58b6ea58-12969\"\r\nCache - Control: max-age=0\r\n\r\n", i);
                //sendDone[i].WaitOne();

                // Receive the response from the remote device.  
                await Receive(client, i);
                //receiveDone[i].WaitOne();

                Thread.Sleep(2000);

                // Write the response to the console.  
                Console.WriteLine("Response received : {0}", response[i]);

                // Release the socket.  
                client.Shutdown(SocketShutdown.Both);
                client.Close();

            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static void ConnectCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the socket from the state object.  
                StateObject s= (StateObject)ar.AsyncState;
                Socket client = s.workSocket;


                // Complete the connection.  
                client.EndConnect(ar);

                Console.WriteLine("Socket connected to {0}",
                    client.RemoteEndPoint.ToString());

                // Signal that the connection has been made.  
                connectDone[s.i].Set();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static async Task Receive(Socket client, int i)
        {
            try
            {
                // Create the state object.  
                StateObject state = new StateObject();
                state.workSocket = client;
                state.i = i;

                // Begin receiving the data from the remote device.  
                client.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                    new AsyncCallback(ReceiveCallback), state);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static int ParseHttpResponse(string str)
        {
            string[] splitted = str.Split(new[] { '\r', '\n' });
            int i, length=0;


            for (i = 1; i < splitted.Length; i++)
            {
                string[] current = splitted[i].Split(new[] { ':' });
                if (current[0].CompareTo("Content-Length") == 0)
                {
                    length = int.Parse(current[1]);
                }
            }

            return length;

        }

        private static async void ReceiveCallback(IAsyncResult ar)
        {
            try
            {
                // Retrieve the state object and the client socket   
                // from the asynchronous state object.  
                StateObject state = (StateObject)ar.AsyncState;
                Socket client = state.workSocket;

                // Read data from the remote device.  
                int bytesRead = client.EndReceive(ar);

                state.sb.Append(Encoding.ASCII.GetString(state.buffer, 0, bytesRead));

                string[] parts = state.sb.ToString().Split(new[] { "\r\n\r\n" }, System.StringSplitOptions.RemoveEmptyEntries);

                if (parts[1].Length < ParseHttpResponse(state.sb.ToString()))
                {
                    


                    // Get the rest of the data.  
                    client.BeginReceive(state.buffer, 0, StateObject.BufferSize, 0,
                    new AsyncCallback( ReceiveCallback), state);
                }
                else
                {
                    // All the data has arrived; put it in response.  
                    if (state.sb.Length > 1)
                    {
                        response[state.i] = state.sb.ToString();
                    }
                    // Signal that all bytes have been received.  
                    receiveDone[state.i].Set();
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        private static async Task Send(Socket client, String data, int i)
        {
            // Convert the string data to byte data using ASCII encoding.  
            byte[] byteData = Encoding.ASCII.GetBytes(data);

            StateObject s = new StateObject()
            {
                workSocket = client,
                i = i,
            };

            // Begin sending the data to the remote device.  
            client.BeginSend(byteData, 0, byteData.Length, 0,
                new AsyncCallback(SendCallback), s);
        }

        private static async void SendCallback(IAsyncResult ar)
        {
            try
            {
                StateObject s = (StateObject)ar.AsyncState;

                // Retrieve the socket from the state object.  
                Socket client = s.workSocket;


                // Complete sending the data to the remote device.  
                int bytesSent = client.EndSend(ar);
                Console.WriteLine("Sent {0} bytes to server.", bytesSent);

                // Signal that all bytes have been sent.  
                sendDone[s.i].Set();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
        }

        static void Main(string[] args)
        {
            

            List<Thread> threads = new List<Thread>();
            ParameterizedThreadStart start = new ParameterizedThreadStart(doStart);
            List<Task> tasks = new List<Task>();

            for (int i = 0; i < 3; i++)
            {
                tasks.Add(Task.Factory.StartNew(doStart, i));
            }
            Task.WaitAll(tasks.ToArray());


        }

        static void doStart(object ar)
        {
            int i = (int)ar;

            StartClient(hostNames[i], i);
        }
    }
}
