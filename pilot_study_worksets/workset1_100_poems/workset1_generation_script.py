import os
import shutil

VOLUME_DIR = 'full_corpus'
OUTPUT_DIR = os.path.join('workset1', 'collection')
os.makedirs(OUTPUT_DIR, exist_ok=True)

os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_022'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015055796364_022', '69.txt')
    fname = page_index.get(69)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 69 in volume mdp.39015055796364')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_027'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_027', '77.txt')
    fname = page_index.get(77)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 77 in volume hvd.hn1nyx')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_027', '78.txt')
    fname = page_index.get(78)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 78 in volume hvd.hn1nyx')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.c065597279_005'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.c065597279')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.c065597279_005', '63.txt')
    fname = page_index.get(63)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 63 in volume uc1.c065597279')
    dst = os.path.join(OUTPUT_DIR, 'uc1.c065597279_005', '64.txt')
    fname = page_index.get(64)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 64 in volume uc1.c065597279')
    dst = os.path.join(OUTPUT_DIR, 'uc1.c065597279_005', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume uc1.c065597279')
os.makedirs(os.path.join(OUTPUT_DIR, 'ien.35556034454629_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'ien.35556034454629')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '81.txt')
    fname = page_index.get(81)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 81 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '82.txt')
    fname = page_index.get(82)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 82 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '83.txt')
    fname = page_index.get(83)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 83 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '84.txt')
    fname = page_index.get(84)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 84 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '86.txt')
    fname = page_index.get(86)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 86 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '87.txt')
    fname = page_index.get(87)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 87 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '88.txt')
    fname = page_index.get(88)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 88 in volume ien.35556034454629')
    dst = os.path.join(OUTPUT_DIR, 'ien.35556034454629_007', '89.txt')
    fname = page_index.get(89)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 89 in volume ien.35556034454629')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_060'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_060', '133.txt')
    fname = page_index.get(133)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 133 in volume loc.ark_13960_t1ng55d1m')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_015', '48.txt')
    fname = page_index.get(48)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 48 in volume mdp.39015048915881')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048915881_015', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015048915881')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.c065597279_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.c065597279')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.c065597279_006', '69.txt')
    fname = page_index.get(69)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 69 in volume uc1.c065597279')
    dst = os.path.join(OUTPUT_DIR, 'uc1.c065597279_006', '70.txt')
    fname = page_index.get(70)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 70 in volume uc1.c065597279')
    dst = os.path.join(OUTPUT_DIR, 'uc1.c065597279_006', '71.txt')
    fname = page_index.get(71)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 71 in volume uc1.c065597279')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_086'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_086', '180.txt')
    fname = page_index.get(180)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 180 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037297051_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037297051')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_007', '33.txt')
    fname = page_index.get(33)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 33 in volume mdp.39015037297051')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_007', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume mdp.39015037297051')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044020016994_005'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044020016994')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_005', '46.txt')
    fname = page_index.get(46)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 46 in volume hvd.32044020016994')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_005', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume hvd.32044020016994')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_005', '48.txt')
    fname = page_index.get(48)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 48 in volume hvd.32044020016994')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_038'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_038', '63.txt')
    fname = page_index.get(63)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 63 in volume mdp.39015041056824')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041016018_003'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041016018')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_003', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015041016018')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_003', '22.txt')
    fname = page_index.get(22)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 22 in volume mdp.39015041016018')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041016018_003', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015041016018')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015059119985_038'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015059119985')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015059119985_038', '74.txt')
    fname = page_index.get(74)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 74 in volume mdp.39015059119985')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015059119985_038', '75.txt')
    fname = page_index.get(75)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 75 in volume mdp.39015059119985')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015059119985_038', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume mdp.39015059119985')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_020'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037873620')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037873620_020', '75.txt')
    fname = page_index.get(75)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 75 in volume mdp.39015037873620')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062487973_003'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062487973')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062487973_003', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015062487973')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_053'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_053', '140.txt')
    fname = page_index.get(140)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 140 in volume mdp.39015078805275')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058271480_009', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000068225810_011'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000068225810')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000068225810_011', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume pst.000068225810')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106006951187_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106006951187')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_017', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume uc1.32106006951187')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_017', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume uc1.32106006951187')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '48.txt')
    fname = page_index.get(48)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 48 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '49.txt')
    fname = page_index.get(49)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 49 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '50.txt')
    fname = page_index.get(50)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 50 in volume mdp.39015062571636')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '51.txt')
    fname = page_index.get(51)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 51 in volume mdp.39015062571636')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015051278813_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015051278813')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_004', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_004', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_004', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_004', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume mdp.39015051278813')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_022'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_022', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume dul1.ark_13960_t3f00205w')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048918893_030'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048918893')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_030', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015048918893')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_030', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015048918893')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_021'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058271480_021', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015010733783_016'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_016', '95.txt')
    fname = page_index.get(95)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 95 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_016', '96.txt')
    fname = page_index.get(96)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 96 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_016', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume mdp.39015010733783')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015010733783_016', '98.txt')
    fname = page_index.get(98)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 98 in volume mdp.39015010733783')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
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
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078788448_028'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078788448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_028', '95.txt')
    fname = page_index.get(95)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 95 in volume mdp.39015078788448')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_028', '96.txt')
    fname = page_index.get(96)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 96 in volume mdp.39015078788448')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_028', '97.txt')
    fname = page_index.get(97)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 97 in volume mdp.39015078788448')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_022'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_022', '103.txt')
    fname = page_index.get(103)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 103 in volume hvd.32044050812528')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_022', '104.txt')
    fname = page_index.get(104)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 104 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_015', '51.txt')
    fname = page_index.get(51)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 51 in volume loc.ark_13960_t1ng55d1m')
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_015', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume loc.ark_13960_t1ng55d1m')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111037739_030'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111037739')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
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
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_006', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uiuc.99685572812205899')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_001', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume uiuc.99685572812205899')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015025340269_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015025340269')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015025340269_006', '20.txt')
    fname = page_index.get(20)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 20 in volume mdp.39015025340269')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_071'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_071', '163.txt')
    fname = page_index.get(163)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 163 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_071', '164.txt')
    fname = page_index.get(164)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 164 in volume mdp.39015037332130')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '152.txt')
    fname = page_index.get(152)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 152 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '153.txt')
    fname = page_index.get(153)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 153 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '154.txt')
    fname = page_index.get(154)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 154 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '155.txt')
    fname = page_index.get(155)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 155 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '156.txt')
    fname = page_index.get(156)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 156 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '157.txt')
    fname = page_index.get(157)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 157 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '158.txt')
    fname = page_index.get(158)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 158 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '159.txt')
    fname = page_index.get(159)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 159 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '160.txt')
    fname = page_index.get(160)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 160 in volume mdp.39015038896729')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015038896729_075', '161.txt')
    fname = page_index.get(161)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 161 in volume mdp.39015038896729')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_031'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_031', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015041056824')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106006951187_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106006951187')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106006951187_001', '11.txt')
    fname = page_index.get(11)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 11 in volume uc1.32106006951187')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_034'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_034', '137.txt')
    fname = page_index.get(137)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 137 in volume loc.ark_13960_t4pk0ws6x')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106018768926_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106018768926')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_017', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume uc1.32106018768926')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_026'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_026', '61.txt')
    fname = page_index.get(61)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 61 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066805063_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066805063')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066805063_015', '32.txt')
    fname = page_index.get(32)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 32 in volume mdp.39015066805063')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078788448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031', '101.txt')
    fname = page_index.get(101)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 101 in volume mdp.39015078788448')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031', '102.txt')
    fname = page_index.get(102)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 102 in volume mdp.39015078788448')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031', '103.txt')
    fname = page_index.get(103)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 103 in volume mdp.39015078788448')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106018768926_022'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106018768926')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_022', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume uc1.32106018768926')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106018768926_022', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume uc1.32106018768926')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_001', '47.txt')
    fname = page_index.get(47)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 47 in volume loc.ark_13960_t4pk0ws6x')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037297051_032'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037297051')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_032', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume mdp.39015037297051')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_059'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_059', '132.txt')
    fname = page_index.get(132)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 132 in volume loc.ark_13960_t1ng55d1m')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_042'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015049644100_042', '145.txt')
    fname = page_index.get(145)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 145 in volume mdp.39015049644100')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015051278813_022'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015051278813')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_022', '64.txt')
    fname = page_index.get(64)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 64 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_022', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_022', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_022', '67.txt')
    fname = page_index.get(67)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 67 in volume mdp.39015051278813')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041101133_024'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
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
os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173018279060_027'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173018279060')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'txu.059173018279060_027', '83.txt')
    fname = page_index.get(83)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 83 in volume txu.059173018279060')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173018279060_027', '84.txt')
    fname = page_index.get(84)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 84 in volume txu.059173018279060')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173018279060_027', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume txu.059173018279060')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173018279060_027', '86.txt')
    fname = page_index.get(86)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 86 in volume txu.059173018279060')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173018279060_027', '87.txt')
    fname = page_index.get(87)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 87 in volume txu.059173018279060')
    dst = os.path.join(OUTPUT_DIR, 'txu.059173018279060_027', '88.txt')
    fname = page_index.get(88)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 88 in volume txu.059173018279060')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024796545_036'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024796545')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015024796545_036', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume mdp.39015024796545')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_007', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume dul1.ark_13960_s2st3fdcwc7')
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_007', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume dul1.ark_13960_s2st3fdcwc7')
    dst = os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_007', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume dul1.ark_13960_s2st3fdcwc7')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_028'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_028', '79.txt')
    fname = page_index.get(79)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 79 in volume hvd.hn1nyx')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_028', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume hvd.hn1nyx')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044080899966')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
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
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_041'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015084107047_041', '79.txt')
    fname = page_index.get(79)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 79 in volume mdp.39015084107047')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060820183_021'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060820183')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060820183_021', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume mdp.39015060820183')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015060820183_021', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015060820183')
os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_013'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_013', '33.txt')
    fname = page_index.get(33)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 33 in volume ucbk.ark_28722_h20g3h67c')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_018'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015021471480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
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
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015051278813_019'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015051278813')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_019', '58.txt')
    fname = page_index.get(58)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 58 in volume mdp.39015051278813')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015051278813_019', '59.txt')
    fname = page_index.get(59)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 59 in volume mdp.39015051278813')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_019'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_019', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015008570940')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044020016994_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044020016994')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_001', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume hvd.32044020016994')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_001', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume hvd.32044020016994')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_001', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume hvd.32044020016994')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_001', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume hvd.32044020016994')
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044020016994_001', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume hvd.32044020016994')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_011'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_011', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015058068860')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_014'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_014', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume mdp.39015047858124')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_014', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015047858124')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_033'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'inu.30000107605259_033', '76.txt')
    fname = page_index.get(76)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 76 in volume inu.30000107605259')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034908049_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034908049')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034908049_015', '79.txt')
    fname = page_index.get(79)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 79 in volume mdp.39015034908049')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015034908049_015', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume mdp.39015034908049')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_021'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015058068860_021', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume mdp.39015058068860')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066805063_031'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066805063')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066805063_031', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume mdp.39015066805063')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037297051_024'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037297051')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037297051_024', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume mdp.39015037297051')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048918893_023'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048918893')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015048918893_023', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume mdp.39015048918893')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_028'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015041056824_028', '50.txt')
    fname = page_index.get(50)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 50 in volume mdp.39015041056824')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069361874_035'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069361874')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_035', '73.txt')
    fname = page_index.get(73)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 73 in volume mdp.39015069361874')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_035', '74.txt')
    fname = page_index.get(74)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 74 in volume mdp.39015069361874')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066844294_024'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066844294')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066844294_024', '55.txt')
    fname = page_index.get(55)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 55 in volume mdp.39015066844294')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066844294_024', '56.txt')
    fname = page_index.get(56)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 56 in volume mdp.39015066844294')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015066844294_024', '57.txt')
    fname = page_index.get(57)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 57 in volume mdp.39015066844294')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037759605_019'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037759605_019', '98.txt')
    fname = page_index.get(98)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 98 in volume mdp.39015037759605')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001132199_018'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001132199')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'emu.010001132199_018', '43.txt')
    fname = page_index.get(43)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 43 in volume emu.010001132199')
    dst = os.path.join(OUTPUT_DIR, 'emu.010001132199_018', '44.txt')
    fname = page_index.get(44)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 44 in volume emu.010001132199')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056944013_033'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056944013')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056944013_033', '65.txt')
    fname = page_index.get(65)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 65 in volume mdp.39015056944013')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056944013_033', '66.txt')
    fname = page_index.get(66)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 66 in volume mdp.39015056944013')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_077'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_077', '188.txt')
    fname = page_index.get(188)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 188 in volume mdp.39015046852540')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056652319_025'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056652319')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056652319_025', '79.txt')
    fname = page_index.get(79)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 79 in volume mdp.39015056652319')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056652319_025', '80.txt')
    fname = page_index.get(80)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 80 in volume mdp.39015056652319')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015056652319_025', '81.txt')
    fname = page_index.get(81)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 81 in volume mdp.39015056652319')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_049'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_049', '134.txt')
    fname = page_index.get(134)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 134 in volume mdp.39015078805275')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_049', '135.txt')
    fname = page_index.get(135)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 135 in volume mdp.39015078805275')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078805275_049', '136.txt')
    fname = page_index.get(136)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 136 in volume mdp.39015078805275')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019480612')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_009', '33.txt')
    fname = page_index.get(33)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 33 in volume uc1.32106019480612')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_009', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume uc1.32106019480612')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_040'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_040', '90.txt')
    fname = page_index.get(90)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 90 in volume mdp.39015047858124')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_044'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015047858124_044', '95.txt')
    fname = page_index.get(95)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 95 in volume mdp.39015047858124')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_013'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019480612')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_013', '39.txt')
    fname = page_index.get(39)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 39 in volume uc1.32106019480612')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019480612_013', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume uc1.32106019480612')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_072'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_072', '189.txt')
    fname = page_index.get(189)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 189 in volume pst.000006235918')
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_072', '190.txt')
    fname = page_index.get(190)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 190 in volume pst.000006235918')
    dst = os.path.join(OUTPUT_DIR, 'pst.000006235918_072', '191.txt')
    fname = page_index.get(191)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 191 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_029'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_029', '52.txt')
    fname = page_index.get(52)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 52 in volume ucbk.ark_28722_h20g3h67c')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062522811_025'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062522811')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_025', '107.txt')
    fname = page_index.get(107)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 107 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_025', '108.txt')
    fname = page_index.get(108)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 108 in volume mdp.39015062522811')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019144424_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019144424_001', '15.txt')
    fname = page_index.get(15)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 15 in volume uc1.32106019144424')
    dst = os.path.join(OUTPUT_DIR, 'uc1.32106019144424_001', '16.txt')
    fname = page_index.get(16)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 16 in volume uc1.32106019144424')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062522811')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '23.txt')
    fname = page_index.get(23)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 23 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '24.txt')
    fname = page_index.get(24)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 24 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '25.txt')
    fname = page_index.get(25)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 25 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '26.txt')
    fname = page_index.get(26)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 26 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '27.txt')
    fname = page_index.get(27)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 27 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '29.txt')
    fname = page_index.get(29)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 29 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '30.txt')
    fname = page_index.get(30)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 30 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '31.txt')
    fname = page_index.get(31)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 31 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '32.txt')
    fname = page_index.get(32)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 32 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '33.txt')
    fname = page_index.get(33)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 33 in volume mdp.39015062522811')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015062522811_004', '34.txt')
    fname = page_index.get(34)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 34 in volume mdp.39015062522811')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078788448_033'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078788448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015078788448_033', '107.txt')
    fname = page_index.get(107)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 107 in volume mdp.39015078788448')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_035'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.32044050812528_035', '121.txt')
    fname = page_index.get(121)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 121 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015042085947_012'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015042085947_012', '28.txt')
    fname = page_index.get(28)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 28 in volume mdp.39015042085947')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032762174_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015032762174_004', '21.txt')
    fname = page_index.get(21)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 21 in volume mdp.39015032762174')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_095'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_095', '224.txt')
    fname = page_index.get(224)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 224 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_095', '225.txt')
    fname = page_index.get(225)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 225 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_095', '226.txt')
    fname = page_index.get(226)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 226 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_095', '227.txt')
    fname = page_index.get(227)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 227 in volume mdp.39015046852540')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015046852540_095', '228.txt')
    fname = page_index.get(228)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 228 in volume mdp.39015046852540')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069361874_016'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015069361874')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_016', '40.txt')
    fname = page_index.get(40)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 40 in volume mdp.39015069361874')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_016', '41.txt')
    fname = page_index.get(41)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 41 in volume mdp.39015069361874')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015069361874_016', '42.txt')
    fname = page_index.get(42)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 42 in volume mdp.39015069361874')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_023'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
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
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037332130_049'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037332130')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_049', '117.txt')
    fname = page_index.get(117)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 117 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_049', '118.txt')
    fname = page_index.get(118)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 118 in volume mdp.39015037332130')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015037332130_049', '119.txt')
    fname = page_index.get(119)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 119 in volume mdp.39015037332130')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_031'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_031', '85.txt')
    fname = page_index.get(85)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 85 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_031', '86.txt')
    fname = page_index.get(86)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 86 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_031', '87.txt')
    fname = page_index.get(87)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 87 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_031', '88.txt')
    fname = page_index.get(88)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 88 in volume mdp.39015008570940')
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_031', '89.txt')
    fname = page_index.get(89)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 89 in volume mdp.39015008570940')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_030'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_030', '74.txt')
    fname = page_index.get(74)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 74 in volume loc.ark_13960_t1ng55d1m')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_084'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015040135538_084', '175.txt')
    fname = page_index.get(175)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 175 in volume mdp.39015040135538')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_021'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015008570940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'mdp.39015008570940_021', '69.txt')
    fname = page_index.get(69)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 69 in volume mdp.39015008570940')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_014'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
else:
    page_index = {}
    for fname in os.listdir(volume_dir):
        base = fname.split('.')[0]
        try:
            page_num = int(base.lstrip('0') or '0')
        except ValueError:
            continue
        page_index[page_num] = fname
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_014', '53.txt')
    fname = page_index.get(53)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 53 in volume hvd.hn1nyx')
    dst = os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_014', '54.txt')
    fname = page_index.get(54)
    if fname:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, dst)
    else:
        print('Missing page 54 in volume hvd.hn1nyx')
