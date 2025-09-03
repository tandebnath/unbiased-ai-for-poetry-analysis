import os
import shutil

VOLUME_DIR = 'full_corpus'
OUTPUT_DIR = os.path.join('workset2', 'collection')
os.makedirs(OUTPUT_DIR, exist_ok=True)

volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_041'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_041', '69.txt')
    fname = page_index.get(69)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 69 in volume mdp.39015058068860')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_010', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015049644100')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_010', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume mdp.39015049644100')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015019441578')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '32.txt')
    fname = page_index.get(32)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 32 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_001', '33.txt')
    fname = page_index.get(33)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 33 in volume mdp.39015019441578')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001297436')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001297436_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010001297436_002', '167.txt')
    fname = page_index.get(167)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 167 in volume emu.010001297436')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_005', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015078805275')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015073926746_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015073926746_011', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015073926746')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015073926746_011', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015073926746')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058066179')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058066179_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058066179_006', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015058066179')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058066179_006', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015058066179')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062625937')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062625937_035'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062625937_035', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume mdp.39015062625937')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_037'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_037', '61.txt')
    fname = page_index.get(61)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 61 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111363671')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111363671_018'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000111363671_018', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume inu.30000111363671')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_077'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_077', '107.txt')
    fname = page_index.get(107)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 107 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_071'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_071', '134.txt')
    fname = page_index.get(134)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 134 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_033', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015041056824')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037873620')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_007'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_007', '37.txt')
    fname = page_index.get(37)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 37 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_007', '38.txt')
    fname = page_index.get(38)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 38 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_007', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015037873620')
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_010', '68.txt')
    fname = page_index.get(68)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 68 in volume loc.ark_13960_t4pk0ws6x')
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_010', '69.txt')
    fname = page_index.get(69)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 69 in volume loc.ark_13960_t4pk0ws6x')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_032'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058271480_032', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.39015058271480')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015021471480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015021471480_012', '36.txt')
    fname = page_index.get(36)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 36 in volume mdp.39015021471480')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015021471480_012', '37.txt')
    fname = page_index.get(37)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 37 in volume mdp.39015021471480')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040730916')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040730916_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_008', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015040730916')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_008', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015040730916')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_027'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_027', '93.txt')
    fname = page_index.get(93)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 93 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_027', '94.txt')
    fname = page_index.get(94)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 94 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_027', '95.txt')
    fname = page_index.get(95)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 95 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056652319')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056652319_032'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056652319_032', '95.txt')
    fname = page_index.get(95)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 95 in volume mdp.39015056652319')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058271480_005', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015058271480')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037759605_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_025', '104.txt')
    fname = page_index.get(104)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 104 in volume mdp.39015037759605')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_044'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_044', '112.txt')
    fname = page_index.get(112)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 112 in volume mdp.39015008570940')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041101133_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_026', '70.txt')
    fname = page_index.get(70)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 70 in volume mdp.39015041101133')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_026', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume mdp.39015041101133')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041101133_026', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume mdp.39015041101133')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_028', '269.txt')
    fname = page_index.get(269)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 269 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_028', '270.txt')
    fname = page_index.get(270)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 270 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034908049')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034908049_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034908049_033', '145.txt')
    fname = page_index.get(145)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 145 in volume mdp.39015034908049')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_043'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_043', '103.txt')
    fname = page_index.get(103)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 103 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_002', '81.txt')
    fname = page_index.get(81)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 81 in volume hvd.32044050812528')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_089'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_089', '212.txt')
    fname = page_index.get(212)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 212 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_089', '213.txt')
    fname = page_index.get(213)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 213 in volume mdp.39015046852540')
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_014', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume umn.31951d02915219o')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015015347076')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015015347076_020'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_020', '74.txt')
    fname = page_index.get(74)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 74 in volume mdp.39015015347076')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_020', '75.txt')
    fname = page_index.get(75)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 75 in volume mdp.39015015347076')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_051'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_051', '126.txt')
    fname = page_index.get(126)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 126 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_051', '127.txt')
    fname = page_index.get(127)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 127 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_051', '128.txt')
    fname = page_index.get(128)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 128 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_051', '129.txt')
    fname = page_index.get(129)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 129 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_051', '130.txt')
    fname = page_index.get(130)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 130 in volume mdp.39015008570940')
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_013'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_013', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume umn.31951d02915219o')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_067'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_067', '109.txt')
    fname = page_index.get(109)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 109 in volume dul1.ark_13960_t27b3zv3b')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060820183')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060820183_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060820183_019', '50.txt')
    fname = page_index.get(50)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 50 in volume mdp.39015060820183')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_009', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume dul1.ark_13960_t3f00205w')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_092'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_092', '217.txt')
    fname = page_index.get(217)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 217 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_092', '218.txt')
    fname = page_index.get(218)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 218 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_092', '219.txt')
    fname = page_index.get(219)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 219 in volume mdp.39015046852540')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044080899966')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044080899966_009', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume hvd.32044080899966')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015051278813')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015051278813_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_014', '50.txt')
    fname = page_index.get(50)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 50 in volume mdp.39015051278813')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015042085947_023'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_023', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015042085947')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_017'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_017', '61.txt')
    fname = page_index.get(61)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 61 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015003918763')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015003918763_016'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015003918763_016', '90.txt')
    fname = page_index.get(90)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 90 in volume mdp.39015003918763')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034258585_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_011', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015034258585')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_011', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume mdp.39015034258585')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056441465')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056441465_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056441465_006', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015056441465')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024695457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024695457_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_006', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015024695457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_006', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015024695457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037873620')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_030', '105.txt')
    fname = page_index.get(105)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 105 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_030', '106.txt')
    fname = page_index.get(106)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 106 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_030', '107.txt')
    fname = page_index.get(107)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 107 in volume mdp.39015037873620')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_047'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_047', '114.txt')
    fname = page_index.get(114)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 114 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_047', '115.txt')
    fname = page_index.get(115)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 115 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019144424_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019144424_025', '59.txt')
    fname = page_index.get(59)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 59 in volume uc1.32106019144424')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019144424_025', '60.txt')
    fname = page_index.get(60)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 60 in volume uc1.32106019144424')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060820183')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060820183_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060820183_026', '59.txt')
    fname = page_index.get(59)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 59 in volume mdp.39015060820183')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060820183_026', '60.txt')
    fname = page_index.get(60)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 60 in volume mdp.39015060820183')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173009680328')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173009680328_045'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_045', '112.txt')
    fname = page_index.get(112)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 112 in volume txu.059173009680328')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_045', '113.txt')
    fname = page_index.get(113)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 113 in volume txu.059173009680328')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_047'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_047', '151.txt')
    fname = page_index.get(151)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 151 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_047', '152.txt')
    fname = page_index.get(152)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 152 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_047', '153.txt')
    fname = page_index.get(153)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 153 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_047', '154.txt')
    fname = page_index.get(154)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 154 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_047', '155.txt')
    fname = page_index.get(155)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 155 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019109211')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019109211_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019109211_019', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume uc1.32106019109211')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_017'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_017', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_017', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_017', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_017', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_001', '15.txt')
    fname = page_index.get(15)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 15 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_001', '16.txt')
    fname = page_index.get(16)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 16 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_001', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015084107047_011', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume mdp.39015084107047')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_042'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_042', '101.txt')
    fname = page_index.get(101)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 101 in volume mdp.39015040135538')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_042', '102.txt')
    fname = page_index.get(102)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 102 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000068225810')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000068225810_037'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000068225810_037', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume pst.000068225810')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_011', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_081'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_081', '205.txt')
    fname = page_index.get(205)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 205 in volume pst.000006235918')
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_081', '206.txt')
    fname = page_index.get(206)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 206 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_001', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_001', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_029'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_029', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume dul1.ark_13960_t27b3zv3b')
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_029', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume dul1.ark_13960_t27b3zv3b')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_012', '46.txt')
    fname = page_index.get(46)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 46 in volume mdp.39015049644100')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_012', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume mdp.39015049644100')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_054'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_054', '126.txt')
    fname = page_index.get(126)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 126 in volume hvd.hn1nyx')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_010', '37.txt')
    fname = page_index.get(37)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 37 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_008', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_008', '36.txt')
    fname = page_index.get(36)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 36 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_016'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_016', '48.txt')
    fname = page_index.get(48)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 48 in volume mdp.39015040135538')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_016', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_004', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_004', '50.txt')
    fname = page_index.get(50)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 50 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000068225810')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000068225810_044'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000068225810_044', '86.txt')
    fname = page_index.get(86)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 86 in volume pst.000068225810')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_080'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_080', '171.txt')
    fname = page_index.get(171)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 171 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034258585_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_009', '38.txt')
    fname = page_index.get(38)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 38 in volume mdp.39015034258585')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_009', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015034258585')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_009', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015034258585')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_009', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015034258585')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_006', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume mdp.39015049644100')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_045'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_045', '142.txt')
    fname = page_index.get(142)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 142 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_045', '143.txt')
    fname = page_index.get(143)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 143 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024695457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024695457_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_008', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015024695457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_008', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015024695457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_008', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015024695457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015015347076')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015015347076_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_015', '64.txt')
    fname = page_index.get(64)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 64 in volume mdp.39015015347076')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015015347076_015', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume mdp.39015015347076')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032504220')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032504220_034'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032504220_034', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume mdp.39015032504220')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032504220')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032504220_017'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032504220_017', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015032504220')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041008601')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041008601_034'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_034', '96.txt')
    fname = page_index.get(96)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 96 in volume mdp.39015041008601')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_048'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_048', '133.txt')
    fname = page_index.get(133)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 133 in volume mdp.39015078805275')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015025340269')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015025340269_023'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015025340269_023', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015025340269')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015019441578')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015', '78.txt')
    fname = page_index.get(78)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 78 in volume mdp.39015019441578')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_041'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_041', '104.txt')
    fname = page_index.get(104)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 104 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_041', '105.txt')
    fname = page_index.get(105)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 105 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015025340269')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015025340269_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015025340269_015', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume mdp.39015025340269')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_012', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_012', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_012', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_012', '46.txt')
    fname = page_index.get(46)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 46 in volume mdp.39015054273282')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_012', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_044'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_044', '88.txt')
    fname = page_index.get(88)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 88 in volume umn.31951d02915219o')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015054273282')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015054273282_010', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015054273282')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041008601')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041008601_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_015', '56.txt')
    fname = page_index.get(56)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 56 in volume mdp.39015041008601')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_015', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015041008601')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.$b704626')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.$b704626_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_009', '46.txt')
    fname = page_index.get(46)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 46 in volume uc1.$b704626')
    dst = os.path.join(OUTPUT_DIR, 'uc1.$b704626_009', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume uc1.$b704626')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024796545')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024796545_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024796545_006', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015024796545')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058066179')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058066179_013'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058066179_013', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015058066179')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024695457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024695457_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_025', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015024695457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_025', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume mdp.39015024695457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_041'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_041', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_041', '98.txt')
    fname = page_index.get(98)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 98 in volume mdp.39015037332130')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_004', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume dul1.ark_13960_t3f00205w')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037297051')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037297051_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_025', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015037297051')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_025', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015037297051')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044080899966')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_018'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044080899966_018', '38.txt')
    fname = page_index.get(38)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 38 in volume hvd.32044080899966')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_033', '118.txt')
    fname = page_index.get(118)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 118 in volume hvd.32044050812528')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_033', '119.txt')
    fname = page_index.get(119)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 119 in volume hvd.32044050812528')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '36.txt')
    fname = page_index.get(36)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 36 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '37.txt')
    fname = page_index.get(37)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 37 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '38.txt')
    fname = page_index.get(38)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 38 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume mdp.39015037759605')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_004', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015037759605')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_047'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_047', '112.txt')
    fname = page_index.get(112)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 112 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_047', '113.txt')
    fname = page_index.get(113)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 113 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_047', '114.txt')
    fname = page_index.get(114)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 114 in volume mdp.39015037332130')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015063268315_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015063268315_001', '11.txt')
    fname = page_index.get(11)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 11 in volume mdp.39015063268315')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015063268315_001', '12.txt')
    fname = page_index.get(12)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 12 in volume mdp.39015063268315')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015063268315_001', '13.txt')
    fname = page_index.get(13)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 13 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_002', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_002', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056441465')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056441465_024'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056441465_024', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015056441465')
