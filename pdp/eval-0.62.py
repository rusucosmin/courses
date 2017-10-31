#!/usr/bin/env python

##############################################################
#                     (C) SANDULEAC DAN                      #
#                  EVALUATOR   version 0.62                  #
#                 RELEASED UNDER GPL LICENCE                 #
#============================================================#
#             this header is under construction              #
##############################################################



# For python 2.2 backwards compatibility, for yield
from __future__ import generators

import sys, os, stat
# We prefer OptionParser
from optparse import OptionParser
# import getopt
import re
from operator import itemgetter as itg
from os.path import join, isfile, isdir
from tempfile import *
# Shell utilities like copy, move etc
import shutil
#from popen2 import popen4 # stres cu asta
from pprint import pprint
from subprocess import *

"""
TODO:
    * cand folosesc verificator, sa afisez si punctajul (din maxim,
      nu procentual) luat pentru fiecare test
"""


# CONSTANTS

_DIR_TESTE = '/home/dan/teste'

defaults = {
    'time': 1000,
    'memory': 16384,
    'inf': '?-%s.in',
    'outf':'',
    'verif': ''
}

options = {
    'chroot_command': '--chroot', # --copy-libs (don't use unless root)
    'args': [],
    'jrun': 'jrun' # jrun executable
}

punctaje = {}

# Do not modify past this point
# -------------------------------------------------------------
# Basic definitions

__debug = []
ESC = chr(27)
color = {
    'green' : ESC+'[1;32m',
    'green_i' : ESC+'[0;32m',
    'red'   : ESC+'[1;31m',
    'else'  : ESC+'[1;35m',
    'maialb': ESC+'[1;37m',
    'normal': ESC+'[m'
}
def col(c): return color[c]
write = sys.stdout.write

def die(message):
    sys.stderr.write(message + '\n')
    sys.exit(2)

def log_print(message):
    global output
    try:
        if output:
            print >>output, message
    except NameError: pass


def setup_output():
    global output
    output = sys.stdout
    if options['quiet']:
        output = None
    if options['output']:
        output = open(options['output'], 'wt')


def find(root, name, depth = 1, icase = True, type = 'df'):
    """Does a re.match() to test `name' against file_name"""
    dirs = [[]] * 2
    if not isdir(root): return
    dirs[0] = [root]
    for nv in xrange(depth):
        dirs[1] = []
        for dir in dirs[0]:
            if nv < depth-1:
                dirs[1].extend([x for x in
                    [join(dir,file) for file in os.listdir(dir)]
                    if isdir(x)]
            )
            for file in os.listdir(dir):
                m = re.match(name, file, icase and re.I)
                if not m: continue
                fullpath = join(dir, file)
                tip = isfile(fullpath) and 'f' or 'd'
                if tip in type:
                    yield (fullpath, m.groups() and m.groups()[-1])
        dirs[0] = dirs[1]

# Caut dir teste dupa root+path1, path2=ignorecase
def find_dir_teste(root, path, depth = 1):
    """Wrapper for find; Caut dir teste dupa root+path1, path2=ignorecase
    path = (.*/)?(.*) -> (path1, path2)"""
    path1, path2 = re.match("(.*/)?(.*)", path).groups()
    # Changed in 0.62
    # Accept -teste suffix too and DON'T allow partial problem name matches
    path2 += "(-teste)?$"
    try:
        results = find(join(root, path1 or ''), path2, depth=depth, type = 'd')
        # FIXME: what if there are more results!
        return results.next()[0]
    except StopIteration:
        return None

def unixize(a, b=None):
    "Dos2unix done in python"
    f = open(a, 'rt')
    lines = [line.replace('\r', '') for line in f]
    if b:  open(b, 'wt').writelines(lines)
    return lines

def parse_parameters(argv):
    "Parses parameters; uses `defaults` and saves to dict `options`"
    parser = OptionParser(usage="%prog executabil [options]")
    rules = [
        (['-p', '--prob'], {'metavar':'...', 'dest':'path', 'help':'Numele problemei (si directorului de teste)'}),
        (['-n', '--name'], {'dest':'nume', 'help':'numele problemei in teste, daca diferit de -p'}),
        (['-d'],           {'dest':'debug', 'action':"store_true", 'default':False, 'help':'debug pentru testele picate'}),
        (['-t', '--time'], {'type':'int', 'help':'time limit in milisecunde'}),
        (['-m', '--memory'], {'metavar':'MEM', 'type':"int", 'help':'limita memorie, kb'}),
        (['-q', '--quiet'], {'dest':'quiet', 'action':'store_true', 'default':False, 'help':'Nu afiseaza decat scorul'}),
        (['-O'], {'dest':'output', 'help':'Fisier pentru salvarea borderoului'}),
        (['--chroot'],     {'action':'store_true', 'default':False,
                            'help':'''Foloseste chroot (jrun are setuid/esti root)
                            Comanda pt jrun: %s
                            ''' % options['chroot_command']}),
        (['-r', '--repo'], {'action': 'store_true', 'default':False, 'help':'intotdeauna foloseste repository'}),
        (['-i', '--inf'],  {'help':'''Format fisier intrare (default %default)
                                   %s se expandeaza ca numele problemei, ? ca nr testului'''}),
        (['-o', '--outf'], {'help':'Format fisier iesire'}),
        (['--verif'],      {'help':'''Program verificator
                                   Parametri: VERIF fisier.in fisier.out fisier.ok
                                   Returneaza: "mesaj\\n(procent punctaj din max)"
                                   Exemplu: Gresit\\n0 ; sau: OK\\n100'''})
    ]
    for i, j in rules: parser.add_option(*i, **j)
    parser.set_defaults(**defaults)
    (opts, args) = parser.parse_args(argv)
    if len(args) < 1:
        die("Trebuie sa precizezi numele executabilului pe care-l evaluez")
    if len(args) > 1:
        die("Parametru in plus '%s'" % args[1])

    opts.executabil = re.sub('^./', '', args[0])
    nume_tmp = opts.nume or re.sub('.*/', '', opts.executabil)
    # S-A DAT NUMELE ADEVARAT AL PROBLEMEI (SI EVENTUAL CALEA) prin -p
    if opts.path:
        # Daca 'path' e o cale de director.. adaugam ``nume'' la el
        if opts.path.endswith('/'):
            opts.path += nume_tmp
        else:
            # luam numele problemei din `path`, decat din `executabil`
            nume_tmp = re.sub(r'^.*/', '', opts.path)
    else: # compute path for dir_teste from executable
        opts.path = nume_tmp

    opts.executabil = os.path.abspath(opts.executabil)

    # Now mess with dir_teste .. aka options.path
    # If can't find "%PATH" / "%PATH-teste" in current directory, search the repo
    pdirs = filter(isdir, [opts.path, opts.path + '-teste'])
    if opts.repo or not pdirs:
        opts.path = find_dir_teste(_DIR_TESTE, opts.path, 5)
    else:
        # Consider we're not using repo because we found it here
        opts.repo = False
        opts.path = os.path.abspath(pdirs[0]) # Use first possible directory
    if not opts.path:
        die('Cum sa-ti spun.. ai luat-o, ca nu gasesc directoru cu teste.. k 10x bye')
    # Path poate fi incomplet, deci de-abia acuma luam numele din path, daca e cazul
    # FIXED: nume <- path doar daca am facut o cautare in repo
    if not opts.nume:
        opts.nume = opts.repo and re.sub('.*/', r'', opts.path) or nume_tmp.lower()

    # FIXME: daca setam options=, faceam o var locala. asa o fol pe cea globala
    options.update(opts.__dict__)
    if not isfile(options['executabil']):
         die('Error: Nu exista executabilul semnalat pentru evaluat!')


def open_config():
    config = '%(path)s/%(nume)s.cfg' % options
    PARAMETERS = ['inf', 'outf', 'time', 'memory', 'verif']
    if not isfile(config):
        try:
            config = find(options['path'], '.*\.cfg$', type='f').next()[0]
        except StopIteration: pass
    if isfile(config):
        log_print("Using config file `%s`" % config)
        f = open(config, 'r')
        #pprint(options)
        for line in f:
            m = re.search(r'(\w+)\s*=\s*(\S+)', line)
            #print line
            if not m: continue
            key, value = m.groups()
            key = key.lower()
            if key in PARAMETERS and options[key] is defaults.get(key):
                # facem si typecasting ca sa nu-l ia string !!!
                try:
                    options[key] = type(options[key])(value)
                    log_print('[config-file] %s=%s' % (key, value))
                    # Verificatorul trebuie sa fie in directorul de configurare
                    if key == 'verif':
                        options[key] = join(options['path'], value)
                except TypeError:
                    log_print("[config-file] Valoare incorecta pentru `%s', asteptam %s" % \
                            (key, type(options[key])) )
            else:
                if key not in PARAMETERS:
                    log_print('[config-file] Parametru necunoscut %s' % key)
                else:
                    log_print('[config-file] Parametru ignorat %s = %s' % (key,value))
        f.close()

    if not options['outf']:
        options['outf'] = re.sub('.in$', '.ok', options['inf'])
    # ==================================
    # fisierul tests.txt pentru punctaje
    # ==================================
    punc_file = join(options['path'], 'tests.txt')
    if isfile(punc_file):
        try:
            for i in open(punc_file, 'r'):
                pair = i.split(' ')
                punctaje[int(pair[0])] = int(pair[1])
        except BaseException, err:
            die('Eroare in fisierul tests.txt: ' + str(err))

def sanity_check():
    if options['verif']:
        if isfile(options['verif']):
            options['verif'] = os.path.abspath(options['verif'])
            # FIXME: HACK to accept pyc scripts here
            if options['verif'].endswith('.pyc'):
                options['verif'] = ['python', options['verif']]
            else:
                options['verif'] = [options['verif']]
        else:
            print("Programul verificator `%s' nu exista, falling back to lazy diff" % \
                    options['verif'])
            options['verif'] = None

    # shall we chroot ?
    jrun_uid = os.stat(os.popen('which "%(jrun)s"' % options).readline()[:-1])[stat.ST_UID]
    if options['chroot']:
        if jrun_uid == 0 or os.getuid() == 0:
            options['args'].append(options['chroot_command'])
        else:
            die('Nu pot chroot, nu esti root si jrun nu are setuid root')


def compara(input, output, ok):
    """ compara(input, output, ok) -> (mesaj, punctaj/punctaj_max %)
    """
    if not options['verif']:
        # just do the diff, lazy diff, ignore all trailing whitespace
        try:
            ln1 = [i.rstrip(' \n') for i in open(output, 'r')]
        except IOError:
            return 'Lipsa out', False
        ln2 = [i.rstrip(' \n\r') for i in open(ok, 'r')]
        if ln1 == ln2:
            return 'OK', 100
        else:
            return 'Gresit', 0
    else:
        #f, tmp = popen4('%s "%s" "%s" "%s"' % (options['verif'], input, os.path.abspath(output), ok))
        command = options['verif'] + [input, os.path.abspath(output), ok]
        f = Popen(command, stdout=PIPE).stdout
        ln = f.readlines()
        try:
            assert (len(ln) == 2)
            punctaj = int(ln[1])
        except:
            print 'Dump - outputul verificatorului:'
            pprint(ln)
            die('Verificatorul nu urmeaza un format corect')
        assert(0 <= punctaj <= 100)
        exitcode = os.WEXITSTATUS(f.close() or 0)
        if exitcode is 0:
            return ln[0].rstrip('\n'), punctaj
        else:
            return 'Verificator: $?=nonzero', 0


def run_tests():
    passed = total = puncte = 0
    punctaj = {}
    workdir = mkdtemp()
    try:
        shutil.copy(options['executabil'], join(workdir, options['nume']))
    except IOError, err:
        die(str(err))
    user_output = '%s.out' % options['nume']
    os.chdir(workdir)
    rules = {
        '%s': options['nume']
    }
    for k in 'inf', 'outf':
        for old, new in rules.iteritems():
            options[k] = options[k].replace(old, new)
        options[k] = re.escape(options[k])
        options[k] = re.sub(r'\\\?+', '(\d+)', options[k])
        #print options[k]
    #pprint(options)

    files_in = [(int(i[1]), i[0]) for i in iter( \
        find(options['path'], options['inf'], type='f') )]
    files_out = dict((int(i[1]), i[0]) for i in iter( \
        find(options['path'], options['outf'], type='f') ))
    #tests_d = dict( ( i[0], (i[1], files_out.get(i[0])) ) \
    #        for i in files_in )
    #tests = sorted(tests_d.items(), key = itg(0))
    tests = sorted((( tcrt[0], (tcrt[1], files_out.get(tcrt[0])) ) \
            for tcrt in files_in),  key = itg(0))
    #pprint(tests)

    final = []

    for test, (inf, outf) in tests:
        ccolor = 'else'
        verdict = 'Eroare necunoscuta'
        mesaj = ["Testul %d" % test, '']
        if not outf and not options['verif']:
            verdict = 'Nu are .ok'
        else:
            unixize(inf, '%s.in' % options['nume'])
            if isfile(user_output):
                os.remove(user_output)
            rez = os.popen(
                '%(jrun)s -p "%(nume)s" -m %(memory)d -t %(time)d ' % options \
                + ' '.join(options['args'])).readline().strip().split(': ')
            mesaj.extend(rez[1:])
            verdict = rez[0]
        if len(punctaje) > 0:
            mesaj.insert(2, str(punctaje.get(test, '10 d')))
        # daca a rulat cu succes, testam daca nu cumva da `Gresit'
        okay = verdict == 'OK'
        mesaj[1] = verdict
        if okay:
            msg, okay = compara(input = inf, output = user_output, ok = outf)
            mesaj[1] = msg
            if okay < 100 and isfile(user_output) and options['debug']:
                # Maybe cleanup a bit here, use tmp = proc.communicate('\n'.join(unixize(outf)))[0]
                command = ['diff', '-pruN', user_output, '-']
                proc = Popen(command, stdout=PIPE, stdin=PIPE)
                fo, fi = proc.stdin, proc.stdout
                fo.writelines(unixize(outf))
                fo.close()
                __debug.append(''.join(fi))
                fi.close()
        ccolor = okay == 0 and 'red' or \
                 okay == 100 and 'green' or \
                 'green_i'
        punctaj = int(round(punctaje.get(test, 10) * okay / 100.0))
        passed += okay
        if len(punctaje) > 0:
            puncte += punctaj
            mesaj[2] = str(punctaj)
        total += 1
        final.append((mesaj, ccolor))
        # Visual notice of test-passed
        sys.stderr.write(`test` + '. ')
        sys.stderr.flush()
    print

    if not tests:
        _i, _o = options['inf'].replace('(\\d+)', '?'), options['outf'].replace('(\\d+)', '?')
        print('Nu am gasit niciun test in directorul de teste. Format teste asteptat: `%s` si `%s`' % (_i, _o))
        return ([],0)
    if puncte is 0:
        puncte = passed / total
    try:
        shutil.rmtree(workdir)
    except: print('Notice: nu am putut sterge workdir ' + workdir)
    return final, puncte

def show_results(final, puncte):
    if not final:
        die('I have no tests to show.. quitting')
    if 'output' in globals() and output:
        if options['debug']:
            log_print(('='*75 + '\n').join(__debug))

        fields = len(final[0][0])
        lens = [max(len(j[0][i]) for j in final if len(j[0]) > i) + 3 \
            for i in xrange(fields)]
        for line, ccolor in final:
            line = [line[i].ljust(lens[i]) for i in xrange(len(line))]
            # Colorization
            if output.isatty():
                line[1] = col(ccolor) + line[1] + col('normal')
                if len(punctaje):
                    line[2] = (ccolor=='green' and col('maialb') or '') + line[2] + col('normal')
            log_print(''.join(line))
        log_print('Punctaj total: %d' % puncte)

    if ('output' in globals() and output != sys.stdout) or not 'output' in globals():
        print puncte


def print_header():
    log_print("Evaluez `%(executabil)s' folosind directorul `%(path)s'" % options)
    log_print("Numele problemei: %s" % options['nume'])


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parse_parameters(argv[1:])
    setup_output()

    # DIRTY hack to avoid writing these if we're writing to a file
    global output
    tmp = output
    if options['output']: output = None
    print_header()
    open_config()
    output = tmp
    sanity_check()
    final, pct = run_tests()
    show_results(final, pct)

if __name__ == "__main__":
    sys.exit(main())
