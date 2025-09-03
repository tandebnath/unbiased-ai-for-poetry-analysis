import os
import shutil

VOLUME_DIR = 'full_corpus'
OUTPUT_DIR = os.path.join('workset3', 'collection')
os.makedirs(OUTPUT_DIR, exist_ok=True)

volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015030760535')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015030760535_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015030760535_028', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume mdp.39015030760535')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_061'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010000709155_061', '144.txt')
    fname = page_index.get(144)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 144 in volume emu.010000709155')
    dst = os.path.join(OUTPUT_DIR, 'emu.010000709155_061', '145.txt')
    fname = page_index.get(145)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 145 in volume emu.010000709155')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000107605259_014', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume inu.30000107605259')
    dst = os.path.join(OUTPUT_DIR, 'inu.30000107605259_014', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume inu.30000107605259')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_028', '91.txt')
    fname = page_index.get(91)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 91 in volume mdp.39015078805275')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_028', '92.txt')
    fname = page_index.get(92)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 92 in volume mdp.39015078805275')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_028', '93.txt')
    fname = page_index.get(93)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 93 in volume mdp.39015078805275')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015041056824')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015041056824')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume mdp.39015041056824')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019480612')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_005', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume uc1.32106019480612')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_005', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume uc1.32106019480612')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173009680328')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173009680328_027'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_027', '75.txt')
    fname = page_index.get(75)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 75 in volume txu.059173009680328')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_027', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume txu.059173009680328')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_020'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_020', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume mdp.39015047858124')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_020', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015047858124')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041101133_016'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_016', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume mdp.39015041101133')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_016', '48.txt')
    fname = page_index.get(48)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 48 in volume mdp.39015041101133')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015021471480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015021471480_005', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015021471480')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_014', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.$b704626')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.$b704626_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_011', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume uc1.$b704626')
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_011', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume uc1.$b704626')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048750940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048750940_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048750940_004', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015048750940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048750940_004', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015048750940')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_059'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_059', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume dul1.ark_13960_t27b3zv3b')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062625937')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062625937_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062625937_015', '37.txt')
    fname = page_index.get(37)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 37 in volume mdp.39015062625937')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1i81')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1i81_024'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1i81_024', '63.txt')
    fname = page_index.get(63)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 63 in volume hvd.hn1i81')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1i81_024', '64.txt')
    fname = page_index.get(64)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 64 in volume hvd.hn1i81')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037873620')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_039'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_039', '135.txt')
    fname = page_index.get(135)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 135 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_039', '136.txt')
    fname = page_index.get(136)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 136 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_039', '137.txt')
    fname = page_index.get(137)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 137 in volume mdp.39015037873620')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066805063')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066805063_034'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066805063_034', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015066805063')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001132199')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001132199_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010001132199_010', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume emu.010001132199')
    dst = os.path.join(OUTPUT_DIR, 'emu.010001132199_010', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume emu.010001132199')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015028916677')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015028916677_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015028916677_003', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015028916677')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_038'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_038', '100.txt')
    fname = page_index.get(100)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 100 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_038', '101.txt')
    fname = page_index.get(101)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 101 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106018768926')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106018768926_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_028', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume uc1.32106018768926')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173009680328')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173009680328_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_030', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume txu.059173009680328')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_030', '81.txt')
    fname = page_index.get(81)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 81 in volume txu.059173009680328')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041101133_024'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_024', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume mdp.39015041101133')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_024', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015041101133')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_022'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_022', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume mdp.39015078805275')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_022', '81.txt')
    fname = page_index.get(81)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 81 in volume mdp.39015078805275')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015042085947_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_030', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.39015042085947')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_030', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015042085947')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015043788846')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015043788846_024'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_024', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015043788846')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069332370')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069332370_018'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069332370_018', '56.txt')
    fname = page_index.get(56)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 56 in volume mdp.39015069332370')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_030', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.39015041056824')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_055'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_055', '126.txt')
    fname = page_index.get(126)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 126 in volume mdp.39015040135538')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_055', '127.txt')
    fname = page_index.get(127)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 127 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_093'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_093', '187.txt')
    fname = page_index.get(187)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 187 in volume mdp.39015040135538')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_093', '188.txt')
    fname = page_index.get(188)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 188 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_038'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_038', '87.txt')
    fname = page_index.get(87)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 87 in volume loc.ark_13960_t1ng55d1m')
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_038', '88.txt')
    fname = page_index.get(88)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 88 in volume loc.ark_13960_t1ng55d1m')
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_038', '89.txt')
    fname = page_index.get(89)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 89 in volume loc.ark_13960_t1ng55d1m')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041008601')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041008601_007'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_007', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume mdp.39015041008601')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_007', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume mdp.39015041008601')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_004', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_004', '32.txt')
    fname = page_index.get(32)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 32 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106007406611')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106007406611_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106007406611_009', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume uc1.32106007406611')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106007406611_009', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume uc1.32106007406611')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069332370')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069332370_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069332370_002', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015069332370')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106006951187')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106006951187_027'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_027', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume uc1.32106006951187')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_027', '58.txt')
    fname = page_index.get(58)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 58 in volume uc1.32106006951187')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078788448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078788448_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_003', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015078788448')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_003', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015078788448')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032504220')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032504220_042'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032504220_042', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume mdp.39015032504220')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044080899966')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044080899966_015', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume hvd.32044080899966')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_018'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_018', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_040'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_040', '119.txt')
    fname = page_index.get(119)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 119 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_040', '120.txt')
    fname = page_index.get(120)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 120 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_040', '121.txt')
    fname = page_index.get(121)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 121 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015073926746_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015073926746_006', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015073926746')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015073926746_006', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015073926746')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015073926746_006', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015073926746')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015059119985')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015059119985_024'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015059119985_024', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015059119985')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062522811')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062522811_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_003', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_003', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015062522811')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062522811')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062522811_020'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_020', '98.txt')
    fname = page_index.get(98)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 98 in volume mdp.39015062522811')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_052'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_052', '98.txt')
    fname = page_index.get(98)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 98 in volume dul1.ark_13960_t3f00205w')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111363671')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111363671_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000111363671_014', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume inu.30000111363671')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_039'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_039', '104.txt')
    fname = page_index.get(104)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 104 in volume mdp.39015008570940')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015059119985')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015059119985_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015059119985_028', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015059119985')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015059119985_028', '56.txt')
    fname = page_index.get(56)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 56 in volume mdp.39015059119985')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_009', '56.txt')
    fname = page_index.get(56)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 56 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034259393')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034259393_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_012', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015034259393')
volume_dir = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_009', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume ucbk.ark_28722_h20g3h67c')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_029'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_029', '89.txt')
    fname = page_index.get(89)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 89 in volume mdp.39015046852540')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.$b704626')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.$b704626_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_001', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume uc1.$b704626')
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_001', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume uc1.$b704626')
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_001', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume uc1.$b704626')
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_001', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume uc1.$b704626')
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_001', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume uc1.$b704626')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058066179')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058066179_029'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058066179_029', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015058066179')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058066179_029', '68.txt')
    fname = page_index.get(68)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 68 in volume mdp.39015058066179')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_007'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_007', '86.txt')
    fname = page_index.get(86)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 86 in volume hvd.32044050812528')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '215.txt')
    fname = page_index.get(215)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 215 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '216.txt')
    fname = page_index.get(216)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 216 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '217.txt')
    fname = page_index.get(217)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 217 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '218.txt')
    fname = page_index.get(218)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 218 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '219.txt')
    fname = page_index.get(219)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 219 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '220.txt')
    fname = page_index.get(220)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 220 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '221.txt')
    fname = page_index.get(221)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 221 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '222.txt')
    fname = page_index.get(222)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 222 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '223.txt')
    fname = page_index.get(223)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 223 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '224.txt')
    fname = page_index.get(224)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 224 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '225.txt')
    fname = page_index.get(225)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 225 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '226.txt')
    fname = page_index.get(226)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 226 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '227.txt')
    fname = page_index.get(227)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 227 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_023', '228.txt')
    fname = page_index.get(228)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 228 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069332370')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069332370_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069332370_005', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015069332370')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015043788846')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015043788846_007'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_007', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015043788846')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_007', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015043788846')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_020'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_020', '70.txt')
    fname = page_index.get(70)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 70 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_020', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume mdp.39015046852540')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '116.txt')
    fname = page_index.get(116)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 116 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '117.txt')
    fname = page_index.get(117)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 117 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '118.txt')
    fname = page_index.get(118)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 118 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '119.txt')
    fname = page_index.get(119)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 119 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '120.txt')
    fname = page_index.get(120)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 120 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '121.txt')
    fname = page_index.get(121)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 121 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '122.txt')
    fname = page_index.get(122)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 122 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '123.txt')
    fname = page_index.get(123)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 123 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '124.txt')
    fname = page_index.get(124)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 124 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '125.txt')
    fname = page_index.get(125)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 125 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '126.txt')
    fname = page_index.get(126)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 126 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '127.txt')
    fname = page_index.get(127)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 127 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '128.txt')
    fname = page_index.get(128)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 128 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '129.txt')
    fname = page_index.get(129)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 129 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '130.txt')
    fname = page_index.get(130)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 130 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_013', '131.txt')
    fname = page_index.get(131)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 131 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_044'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010000709155_044', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume emu.010000709155')
    dst = os.path.join(OUTPUT_DIR, 'emu.010000709155_044', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume emu.010000709155')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069361874')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069361874_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_006', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015069361874')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_006', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015069361874')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048918893')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048918893_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_025', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015048918893')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_025', '56.txt')
    fname = page_index.get(56)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 56 in volume mdp.39015048918893')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_025', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015048918893')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_007'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_007', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_007', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015037332130')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032762174_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032762174_026', '78.txt')
    fname = page_index.get(78)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 78 in volume mdp.39015032762174')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032762174_026', '79.txt')
    fname = page_index.get(79)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 79 in volume mdp.39015032762174')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032762174_026', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume mdp.39015032762174')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032762174_026', '81.txt')
    fname = page_index.get(81)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 81 in volume mdp.39015032762174')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015030760535')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015030760535_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015030760535_025', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume mdp.39015030760535')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015043788846')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015043788846_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_002', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015043788846')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_002', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015043788846')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_041'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_041', '133.txt')
    fname = page_index.get(133)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 133 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'uiuc.99685572812205899')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_008', '37.txt')
    fname = page_index.get(37)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 37 in volume uiuc.99685572812205899')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015000252448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015000252448_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015000252448_005', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015000252448')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_047'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_047', '116.txt')
    fname = page_index.get(116)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 116 in volume hvd.hn1nyx')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_089'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_089', '121.txt')
    fname = page_index.get(121)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 121 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015021471480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_018'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015021471480_018', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume mdp.39015021471480')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_008', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume pst.000006235918')
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_008', '74.txt')
    fname = page_index.get(74)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 74 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054303139')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054303139_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054303139_001', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015054303139')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041101133_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_019', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015041101133')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_019', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.39015041101133')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_026', '63.txt')
    fname = page_index.get(63)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 63 in volume mdp.39015047858124')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_026', '64.txt')
    fname = page_index.get(64)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 64 in volume mdp.39015047858124')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037297051')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037297051_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_010', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015037297051')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_043'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_043', '84.txt')
    fname = page_index.get(84)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 84 in volume dul1.ark_13960_t3f00205w')
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_043', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume dul1.ark_13960_t3f00205w')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_003', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015049644100')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume mdp.39015047858124')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume mdp.39015047858124')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012', '36.txt')
    fname = page_index.get(36)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 36 in volume mdp.39015047858124')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019480612')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_053'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_053', '116.txt')
    fname = page_index.get(116)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 116 in volume uc1.32106019480612')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_001', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015058068860')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048918893')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048918893_017'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_017', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015048918893')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056944013')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056944013_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056944013_019', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015056944013')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019144424_020'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019144424_020', '51.txt')
    fname = page_index.get(51)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 51 in volume uc1.32106019144424')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_044'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000107605259_044', '92.txt')
    fname = page_index.get(92)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 92 in volume inu.30000107605259')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '105.txt')
    fname = page_index.get(105)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 105 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '106.txt')
    fname = page_index.get(106)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 106 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '107.txt')
    fname = page_index.get(107)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 107 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '108.txt')
    fname = page_index.get(108)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 108 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_030', '132.txt')
    fname = page_index.get(132)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 132 in volume loc.ark_13960_t4pk0ws6x')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '127.txt')
    fname = page_index.get(127)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 127 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '128.txt')
    fname = page_index.get(128)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 128 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '129.txt')
    fname = page_index.get(129)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 129 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '130.txt')
    fname = page_index.get(130)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 130 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '131.txt')
    fname = page_index.get(131)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 131 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '132.txt')
    fname = page_index.get(132)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 132 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '133.txt')
    fname = page_index.get(133)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 133 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '134.txt')
    fname = page_index.get(134)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 134 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '135.txt')
    fname = page_index.get(135)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 135 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '136.txt')
    fname = page_index.get(136)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 136 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '137.txt')
    fname = page_index.get(137)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 137 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '138.txt')
    fname = page_index.get(138)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 138 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '139.txt')
    fname = page_index.get(139)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 139 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '140.txt')
    fname = page_index.get(140)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 140 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '141.txt')
    fname = page_index.get(141)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 141 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '142.txt')
    fname = page_index.get(142)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 142 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '143.txt')
    fname = page_index.get(143)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 143 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '144.txt')
    fname = page_index.get(144)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 144 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '145.txt')
    fname = page_index.get(145)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 145 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_019', '146.txt')
    fname = page_index.get(146)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 146 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_002', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015078774927')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_002', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015042085947_007'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_007', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015042085947')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_007', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015042085947')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_039'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_039', '118.txt')
    fname = page_index.get(118)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 118 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_078'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_078', '149.txt')
    fname = page_index.get(149)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 149 in volume umn.31951d02915219o')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012', '74.txt')
    fname = page_index.get(74)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 74 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012', '75.txt')
    fname = page_index.get(75)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 75 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_012', '78.txt')
    fname = page_index.get(78)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 78 in volume mdp.39015037759605')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069361874')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069361874_037'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_037', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume mdp.39015069361874')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056441465')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056441465_046'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056441465_046', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume mdp.39015056441465')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015015347076')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015015347076_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_026', '84.txt')
    fname = page_index.get(84)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 84 in volume mdp.39015015347076')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_026', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume mdp.39015015347076')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_026', '86.txt')
    fname = page_index.get(86)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 86 in volume mdp.39015015347076')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_026', '87.txt')
    fname = page_index.get(87)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 87 in volume mdp.39015015347076')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_026', '88.txt')
    fname = page_index.get(88)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 88 in volume mdp.39015015347076')
