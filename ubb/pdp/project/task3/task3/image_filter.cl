kernel void image_filter(global uchar* a, global uchar* output, int n) {
    size_t i = get_global_id(0);
    
    if(i * 3 + 2 >= n) {
        return ;
    }
    
    int pixel = i * 3;
    uchar sum = (a[pixel] + a[pixel + 1] + a[pixel + 2]) / 3;
    
    output[pixel] = sum;
    output[pixel + 1] = sum;
    output[pixel + 2] = sum;
}
