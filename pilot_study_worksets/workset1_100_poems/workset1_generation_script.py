import os
import shutil

VOLUME_DIR = 'full_corpus'
OUTPUT_DIR = os.path.join('workset1', 'collection')
os.makedirs(OUTPUT_DIR, exist_ok=True)

volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_021'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_021', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume dul1.ark_13960_s2st3fdcwc7')
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_021', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume dul1.ark_13960_s2st3fdcwc7')
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_021', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume dul1.ark_13960_s2st3fdcwc7')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037873620')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '125.txt')
    fname = page_index.get(125)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 125 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '126.txt')
    fname = page_index.get(126)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 126 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '127.txt')
    fname = page_index.get(127)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 127 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '128.txt')
    fname = page_index.get(128)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 128 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '129.txt')
    fname = page_index.get(129)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 129 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '130.txt')
    fname = page_index.get(130)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 130 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_037', '131.txt')
    fname = page_index.get(131)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 131 in volume mdp.39015037873620')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_019', '59.txt')
    fname = page_index.get(59)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 59 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_033', '62.txt')
    fname = page_index.get(62)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 62 in volume dul1.ark_13960_t27b3zv3b')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015019441578')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015019441578_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_003', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015019441578')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015019441578_003', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015019441578')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_037'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015084107047_037', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume mdp.39015084107047')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015084107047_037', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume mdp.39015084107047')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062522811')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062522811_027'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_027', '110.txt')
    fname = page_index.get(110)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 110 in volume mdp.39015062522811')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034262819')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034262819_024'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034262819_024', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015034262819')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034262819_024', '68.txt')
    fname = page_index.get(68)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 68 in volume mdp.39015034262819')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015084107047_006', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015084107047')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_033', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069332370')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069332370_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069332370_028', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015069332370')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.49015001462457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.49015001462457_015'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.49015001462457_015', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.49015001462457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.49015001462457_015', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.49015001462457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034258585_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_030', '96.txt')
    fname = page_index.get(96)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 96 in volume mdp.39015034258585')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_030', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume mdp.39015034258585')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060820183')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060820183_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060820183_014', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015060820183')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.49015001462457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.49015001462457_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.49015001462457_011', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.49015001462457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.49015001462457_011', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.49015001462457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.49015001462457_011', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.49015001462457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015084107047_005', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015084107047')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_094'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_094', '222.txt')
    fname = page_index.get(222)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 222 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_094', '223.txt')
    fname = page_index.get(223)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 223 in volume mdp.39015046852540')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_042'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_042', '91.txt')
    fname = page_index.get(91)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 91 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_034'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_034', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015058068860')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015063268315_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015063268315_012', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040730916')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040730916_029'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_029', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015040730916')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015043788846')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015043788846_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_009', '32.txt')
    fname = page_index.get(32)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 32 in volume mdp.39015043788846')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_064'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_064', '143.txt')
    fname = page_index.get(143)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 143 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_004', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_004', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_004', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040730916')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040730916_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_026', '61.txt')
    fname = page_index.get(61)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 61 in volume mdp.39015040730916')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_026', '62.txt')
    fname = page_index.get(62)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 62 in volume mdp.39015040730916')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_051'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010000709155_051', '89.txt')
    fname = page_index.get(89)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 89 in volume emu.010000709155')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056944013')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056944013_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056944013_028', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015056944013')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015025340269')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015025340269_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015025340269_014', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015025340269')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_056'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_056', '112.txt')
    fname = page_index.get(112)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 112 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_057'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_057', '133.txt')
    fname = page_index.get(133)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 133 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_057', '134.txt')
    fname = page_index.get(134)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 134 in volume mdp.39015037332130')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037819169')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037819169_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037819169_010', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015037819169')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015028916677')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015028916677_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015028916677_004', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015028916677')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066805063')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066805063_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066805063_030', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015066805063')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044080899966')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044080899966_006', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume hvd.32044080899966')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062522811')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062522811_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_014', '92.txt')
    fname = page_index.get(92)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 92 in volume mdp.39015062522811')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015042085947_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_004', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015042085947')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015013350502')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015013350502_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015013350502_001', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015013350502')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015013350502_001', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015013350502')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173009680328')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173009680328_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_019', '61.txt')
    fname = page_index.get(61)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 61 in volume txu.059173009680328')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_019', '62.txt')
    fname = page_index.get(62)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 62 in volume txu.059173009680328')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015030760535')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015030760535_043'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015030760535_043', '105.txt')
    fname = page_index.get(105)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 105 in volume mdp.39015030760535')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_035'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_035', '58.txt')
    fname = page_index.get(58)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 58 in volume mdp.39015058068860')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034258585_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034258585_003', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015034258585')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_011'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_011', '50.txt')
    fname = page_index.get(50)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 50 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_011', '51.txt')
    fname = page_index.get(51)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 51 in volume mdp.39015008570940')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111037739')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111037739_030'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000111037739_030', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume inu.30000111037739')
    dst = os.path.join(OUTPUT_DIR, 'inu.30000111037739_030', '58.txt')
    fname = page_index.get(58)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 58 in volume inu.30000111037739')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060020230')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060020230_016'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060020230_016', '36.txt')
    fname = page_index.get(36)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 36 in volume mdp.39015060020230')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015011336016')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015011336016_037'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015011336016_037', '87.txt')
    fname = page_index.get(87)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 87 in volume mdp.39015011336016')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_069'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_069', '160.txt')
    fname = page_index.get(160)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 160 in volume mdp.39015037332130')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173014228227')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173014228227_019'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173014228227_019', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume txu.059173014228227')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019480612')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_042'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_042', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume uc1.32106019480612')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_109'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_109', '214.txt')
    fname = page_index.get(214)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 214 in volume mdp.39015040135538')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_109', '215.txt')
    fname = page_index.get(215)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 215 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_008', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume mdp.39015058068860')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015043788846')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015043788846_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015043788846_006', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015043788846')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_066'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_066', '90.txt')
    fname = page_index.get(90)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 90 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_082'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_082', '173.txt')
    fname = page_index.get(173)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 173 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_008'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_008', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_008', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_008', '46.txt')
    fname = page_index.get(46)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 46 in volume mdp.39015008570940')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_053'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_053', '108.txt')
    fname = page_index.get(108)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 108 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_048'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_048', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041008601')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041008601_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_028', '84.txt')
    fname = page_index.get(84)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 84 in volume mdp.39015041008601')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_028', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume mdp.39015041008601')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_066'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_066', '146.txt')
    fname = page_index.get(146)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 146 in volume mdp.39015040135538')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173010296815')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173010296815_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173010296815_012', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume txu.059173010296815')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1i81')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1i81_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1i81_002', '14.txt')
    fname = page_index.get(14)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 14 in volume hvd.hn1i81')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1i81_002', '15.txt')
    fname = page_index.get(15)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 15 in volume hvd.hn1i81')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1i81_002', '16.txt')
    fname = page_index.get(16)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 16 in volume hvd.hn1i81')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1i81_002', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume hvd.hn1i81')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041008601')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041008601_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_012', '46.txt')
    fname = page_index.get(46)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 46 in volume mdp.39015041008601')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_012', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume mdp.39015041008601')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_012', '48.txt')
    fname = page_index.get(48)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 48 in volume mdp.39015041008601')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041008601_012', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015041008601')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_002'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000107605259_002', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume inu.30000107605259')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048750940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048750940_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048750940_006', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015048750940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048750940_006', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015048750940')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_071'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_071', '96.txt')
    fname = page_index.get(96)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 96 in volume mdp.39015029858522')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_071', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001132199')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001132199_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010001132199_009', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume emu.010001132199')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_003', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015078774927')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_003', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058271480_004', '19.txt')
    fname = page_index.get(19)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 19 in volume mdp.39015058271480')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173014228227')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173014228227_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173014228227_004', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume txu.059173014228227')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173014228227_004', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume txu.059173014228227')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_034'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_034', '94.txt')
    fname = page_index.get(94)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 94 in volume mdp.39015055796364')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_034', '95.txt')
    fname = page_index.get(95)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 95 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_017'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_017', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume dul1.ark_13960_t27b3zv3b')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106006951187')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106006951187_016'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_016', '38.txt')
    fname = page_index.get(38)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 38 in volume uc1.32106006951187')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_016', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume uc1.32106006951187')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078788448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078788448_010'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_010', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume mdp.39015078788448')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_010', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015078788448')
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_028'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_028', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume loc.ark_13960_t1ng55d1m')
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_028', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume loc.ark_13960_t1ng55d1m')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032504220')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032504220_029'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032504220_029', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume mdp.39015032504220')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037873620')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_025'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_025', '90.txt')
    fname = page_index.get(90)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 90 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_025', '91.txt')
    fname = page_index.get(91)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 91 in volume mdp.39015037873620')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_025', '92.txt')
    fname = page_index.get(92)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 92 in volume mdp.39015037873620')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_035'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_035', '70.txt')
    fname = page_index.get(70)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 70 in volume mdp.39015078774927')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078774927_035', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_041'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_041', '109.txt')
    fname = page_index.get(109)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 109 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_041', '110.txt')
    fname = page_index.get(110)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 110 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_041', '111.txt')
    fname = page_index.get(111)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 111 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040730916')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040730916_001'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_001', '17.txt')
    fname = page_index.get(17)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 17 in volume mdp.39015040730916')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040730916_001', '18.txt')
    fname = page_index.get(18)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 18 in volume mdp.39015040730916')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062625937')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062625937_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062625937_014', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume mdp.39015062625937')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062625937_014', '35.txt')
    fname = page_index.get(35)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 35 in volume mdp.39015062625937')
volume_dir = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_026'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_026', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume ucbk.ark_28722_h20g3h67c')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106018768926')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106018768926_051'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_051', '125.txt')
    fname = page_index.get(125)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 125 in volume uc1.32106018768926')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_051', '126.txt')
    fname = page_index.get(126)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 126 in volume uc1.32106018768926')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_051', '127.txt')
    fname = page_index.get(127)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 127 in volume uc1.32106018768926')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_051', '128.txt')
    fname = page_index.get(128)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 128 in volume uc1.32106018768926')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_051', '129.txt')
    fname = page_index.get(129)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 129 in volume uc1.32106018768926')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060020230')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060020230_014'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060020230_014', '33.txt')
    fname = page_index.get(33)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 33 in volume mdp.39015060020230')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041016018')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041016018_012'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_012', '63.txt')
    fname = page_index.get(63)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 63 in volume mdp.39015041016018')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_012', '64.txt')
    fname = page_index.get(64)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 64 in volume mdp.39015041016018')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_012', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume mdp.39015041016018')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_012', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015041016018')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_042'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_042', '105.txt')
    fname = page_index.get(105)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 105 in volume hvd.hn1nyx')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_042', '106.txt')
    fname = page_index.get(106)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 106 in volume hvd.hn1nyx')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_042', '107.txt')
    fname = page_index.get(107)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 107 in volume hvd.hn1nyx')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000068225810')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000068225810_027'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000068225810_027', '58.txt')
    fname = page_index.get(58)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 58 in volume pst.000068225810')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041016018')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041016018_005'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_005', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume mdp.39015041016018')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_005', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume mdp.39015041016018')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_053'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010000709155_053', '92.txt')
    fname = page_index.get(92)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 92 in volume emu.010000709155')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_023'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_023', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume mdp.39015049644100')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_023', '72.txt')
    fname = page_index.get(72)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 72 in volume mdp.39015049644100')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_023', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume mdp.39015049644100')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024695457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024695457_038'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_038', '61.txt')
    fname = page_index.get(61)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 61 in volume mdp.39015024695457')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024695457_038', '62.txt')
    fname = page_index.get(62)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 62 in volume mdp.39015024695457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_038'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015029858522_038', '62.txt')
    fname = page_index.get(62)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 62 in volume mdp.39015029858522')
volume_dir = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_040'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_040', '69.txt')
    fname = page_index.get(69)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 69 in volume ucbk.ark_28722_h20g3h67c')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034259393')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034259393_009'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_009', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015034259393')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_009', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015034259393')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_009', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume mdp.39015034259393')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_009', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015034259393')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_009', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume mdp.39015034259393')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034259393')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034259393_004'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_004', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume mdp.39015034259393')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048750940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048750940_016'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048750940_016', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015048750940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048750940_016', '45.txt')
    fname = page_index.get(45)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 45 in volume mdp.39015048750940')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_033', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume mdp.39015038896729')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_003'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_003', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_003', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_003', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173009680328')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173009680328_029'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_029', '78.txt')
    fname = page_index.get(78)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 78 in volume txu.059173009680328')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173009680328_029', '79.txt')
    fname = page_index.get(79)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 79 in volume txu.059173009680328')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015003918763')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015003918763_034'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015003918763_034', '120.txt')
    fname = page_index.get(120)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 120 in volume mdp.39015003918763')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034259393')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034259393_033'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_033', '91.txt')
    fname = page_index.get(91)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 91 in volume mdp.39015034259393')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034259393_033', '92.txt')
    fname = page_index.get(92)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 92 in volume mdp.39015034259393')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001132199')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001132199_006'), exist_ok=True)
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010001132199_006', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume emu.010001132199')
