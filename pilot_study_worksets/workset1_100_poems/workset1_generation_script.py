import os
import shutil

VOLUME_DIR = 'Volumes'
OUTPUT_DIR = os.path.join('MyPoemAssignments', 'Collection')
os.makedirs(OUTPUT_DIR, exist_ok=True)

os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_040'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 69:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010000709155_040', '69.txt'))
        found = True
        break
if not found:
    print('Missing page 69 in volume emu.010000709155')
os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173018279060_024'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173018279060')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 73:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173018279060_024', '73.txt'))
        found = True
        break
if not found:
    print('Missing page 73 in volume txu.059173018279060')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173018279060')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 74:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173018279060_024', '74.txt'))
        found = True
        break
if not found:
    print('Missing page 74 in volume txu.059173018279060')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173018279060')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 75:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173018279060_024', '75.txt'))
        found = True
        break
if not found:
    print('Missing page 75 in volume txu.059173018279060')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173018279060')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 76:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173018279060_024', '76.txt'))
        found = True
        break
if not found:
    print('Missing page 76 in volume txu.059173018279060')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 105:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '105.txt'))
        found = True
        break
if not found:
    print('Missing page 105 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 106:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '106.txt'))
        found = True
        break
if not found:
    print('Missing page 106 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 107:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '107.txt'))
        found = True
        break
if not found:
    print('Missing page 107 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 108:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_040', '108.txt'))
        found = True
        break
if not found:
    print('Missing page 108 in volume mdp.39015048915881')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 21:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_004', '21.txt'))
        found = True
        break
if not found:
    print('Missing page 21 in volume mdp.39015047858124')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015047858124')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 22:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_004', '22.txt'))
        found = True
        break
if not found:
    print('Missing page 22 in volume mdp.39015047858124')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_066'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 108:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_066', '108.txt'))
        found = True
        break
if not found:
    print('Missing page 108 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019144424_016'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 44:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019144424_016', '44.txt'))
        found = True
        break
if not found:
    print('Missing page 44 in volume uc1.32106019144424')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 45:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019144424_016', '45.txt'))
        found = True
        break
if not found:
    print('Missing page 45 in volume uc1.32106019144424')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 54:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '54.txt'))
        found = True
        break
if not found:
    print('Missing page 54 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 55:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '55.txt'))
        found = True
        break
if not found:
    print('Missing page 55 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 58:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '58.txt'))
        found = True
        break
if not found:
    print('Missing page 58 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 59:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '59.txt'))
        found = True
        break
if not found:
    print('Missing page 59 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 60:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_004', '60.txt'))
        found = True
        break
if not found:
    print('Missing page 60 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000068225810_038'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000068225810')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 78:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000068225810_038', '78.txt'))
        found = True
        break
if not found:
    print('Missing page 78 in volume pst.000068225810')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015011336016_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015011336016')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 50:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015011336016_017', '50.txt'))
        found = True
        break
if not found:
    print('Missing page 50 in volume mdp.39015011336016')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015011336016')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 51:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015011336016_017', '51.txt'))
        found = True
        break
if not found:
    print('Missing page 51 in volume mdp.39015011336016')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_067'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 147:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015040135538_067', '147.txt'))
        found = True
        break
if not found:
    print('Missing page 147 in volume mdp.39015040135538')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_040'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 62:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058271480_040', '62.txt'))
        found = True
        break
if not found:
    print('Missing page 62 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066844294_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066844294')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015066844294_017', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume mdp.39015066844294')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066844294')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 40:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015066844294_017', '40.txt'))
        found = True
        break
if not found:
    print('Missing page 40 in volume mdp.39015066844294')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015073926746_010'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 26:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_010', '26.txt'))
        found = True
        break
if not found:
    print('Missing page 26 in volume mdp.39015073926746')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 27:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_010', '27.txt'))
        found = True
        break
if not found:
    print('Missing page 27 in volume mdp.39015073926746')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_036'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015021471480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 76:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_036', '76.txt'))
        found = True
        break
if not found:
    print('Missing page 76 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_033'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 67:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_033', '67.txt'))
        found = True
        break
if not found:
    print('Missing page 67 in volume dul1.ark_13960_t3f00205w')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 23:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010000709155_006', '23.txt'))
        found = True
        break
if not found:
    print('Missing page 23 in volume emu.010000709155')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 29:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013', '29.txt'))
        found = True
        break
if not found:
    print('Missing page 29 in volume mdp.39015041056824')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 30:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013', '30.txt'))
        found = True
        break
if not found:
    print('Missing page 30 in volume mdp.39015041056824')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041056824')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041056824_013', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015041056824')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_032'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058271480')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 54:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058271480_032', '54.txt'))
        found = True
        break
if not found:
    print('Missing page 54 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044080899966')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 35:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044080899966_015', '35.txt'))
        found = True
        break
if not found:
    print('Missing page 35 in volume hvd.32044080899966')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015073926746_029'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 64:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_029', '64.txt'))
        found = True
        break
if not found:
    print('Missing page 64 in volume mdp.39015073926746')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_023'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 45:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010000709155_023', '45.txt'))
        found = True
        break
if not found:
    print('Missing page 45 in volume emu.010000709155')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034258585_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 30:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034258585_007', '30.txt'))
        found = True
        break
if not found:
    print('Missing page 30 in volume mdp.39015034258585')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034258585_007', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015034258585')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034258585')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 32:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034258585_007', '32.txt'))
        found = True
        break
if not found:
    print('Missing page 32 in volume mdp.39015034258585')
os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173010296815_016'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173010296815')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 36:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173010296815_016', '36.txt'))
        found = True
        break
if not found:
    print('Missing page 36 in volume txu.059173010296815')
volume_dir = os.path.join(VOLUME_DIR, 'txu.059173010296815')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 37:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173010296815_016', '37.txt'))
        found = True
        break
if not found:
    print('Missing page 37 in volume txu.059173010296815')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111363671_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111363671')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 19:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000111363671_006', '19.txt'))
        found = True
        break
if not found:
    print('Missing page 19 in volume inu.30000111363671')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111363671')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 20:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000111363671_006', '20.txt'))
        found = True
        break
if not found:
    print('Missing page 20 in volume inu.30000111363671')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041101133_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 30:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041101133_009', '30.txt'))
        found = True
        break
if not found:
    print('Missing page 30 in volume mdp.39015041101133')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041101133')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041101133_009', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015041101133')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 27:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010000709155_009', '27.txt'))
        found = True
        break
if not found:
    print('Missing page 27 in volume emu.010000709155')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055901683_013'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055901683')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 60:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055901683_013', '60.txt'))
        found = True
        break
if not found:
    print('Missing page 60 in volume mdp.39015055901683')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055901683')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 61:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055901683_013', '61.txt'))
        found = True
        break
if not found:
    print('Missing page 61 in volume mdp.39015055901683')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_033'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 75:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_033', '75.txt'))
        found = True
        break
if not found:
    print('Missing page 75 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015066805063_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015066805063')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 37:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015066805063_017', '37.txt'))
        found = True
        break
if not found:
    print('Missing page 37 in volume mdp.39015066805063')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000022309136_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000022309136')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 9:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000022309136_001', '9.txt'))
        found = True
        break
if not found:
    print('Missing page 9 in volume inu.30000022309136')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_026'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 52:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078774927_026', '52.txt'))
        found = True
        break
if not found:
    print('Missing page 52 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 53:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078774927_026', '53.txt'))
        found = True
        break
if not found:
    print('Missing page 53 in volume mdp.39015078774927')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034259393_012'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034259393')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 49:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034259393_012', '49.txt'))
        found = True
        break
if not found:
    print('Missing page 49 in volume mdp.39015034259393')
os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 19:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_001', '19.txt'))
        found = True
        break
if not found:
    print('Missing page 19 in volume ucbk.ark_28722_h20g3h67c')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 83:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044050812528_004', '83.txt'))
        found = True
        break
if not found:
    print('Missing page 83 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_041'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 90:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015038896729_041', '90.txt'))
        found = True
        break
if not found:
    print('Missing page 90 in volume mdp.39015038896729')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_036'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 101:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015046852540_036', '101.txt'))
        found = True
        break
if not found:
    print('Missing page 101 in volume mdp.39015046852540')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_044'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015046852540')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 112:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015046852540_044', '112.txt'))
        found = True
        break
if not found:
    print('Missing page 112 in volume mdp.39015046852540')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_044'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 92:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000107605259_044', '92.txt'))
        found = True
        break
if not found:
    print('Missing page 92 in volume inu.30000107605259')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_008'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_008', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015073926746_041'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 87:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_041', '87.txt'))
        found = True
        break
if not found:
    print('Missing page 87 in volume mdp.39015073926746')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 88:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_041', '88.txt'))
        found = True
        break
if not found:
    print('Missing page 88 in volume mdp.39015073926746')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015073926746')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 89:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_041', '89.txt'))
        found = True
        break
if not found:
    print('Missing page 89 in volume mdp.39015073926746')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_042'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015049644100')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 145:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015049644100_042', '145.txt'))
        found = True
        break
if not found:
    print('Missing page 145 in volume mdp.39015049644100')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055901683_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055901683')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 23:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055901683_001', '23.txt'))
        found = True
        break
if not found:
    print('Missing page 23 in volume mdp.39015055901683')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055901683')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055901683_001', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume mdp.39015055901683')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_012'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058068860_012', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015058068860')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_035'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 105:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078805275_035', '105.txt'))
        found = True
        break
if not found:
    print('Missing page 105 in volume mdp.39015078805275')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078805275')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 106:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078805275_035', '106.txt'))
        found = True
        break
if not found:
    print('Missing page 106 in volume mdp.39015078805275')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 89:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_017', '89.txt'))
        found = True
        break
if not found:
    print('Missing page 89 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015003918763_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015003918763')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 72:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015003918763_009', '72.txt'))
        found = True
        break
if not found:
    print('Missing page 72 in volume mdp.39015003918763')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_027'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 80:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055796364_027', '80.txt'))
        found = True
        break
if not found:
    print('Missing page 80 in volume mdp.39015055796364')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015055796364')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 81:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055796364_027', '81.txt'))
        found = True
        break
if not found:
    print('Missing page 81 in volume mdp.39015055796364')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044134446327_005'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044134446327')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 17:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044134446327_005', '17.txt'))
        found = True
        break
if not found:
    print('Missing page 17 in volume hvd.32044134446327')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060020230_029'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060020230')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 59:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060020230_029', '59.txt'))
        found = True
        break
if not found:
    print('Missing page 59 in volume mdp.39015060020230')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015060020230')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 60:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060020230_029', '60.txt'))
        found = True
        break
if not found:
    print('Missing page 60 in volume mdp.39015060020230')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 32:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_006', '32.txt'))
        found = True
        break
if not found:
    print('Missing page 32 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 33:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_006', '33.txt'))
        found = True
        break
if not found:
    print('Missing page 33 in volume mdp.39015048915881')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048750940_026'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048750940')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 63:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048750940_026', '63.txt'))
        found = True
        break
if not found:
    print('Missing page 63 in volume mdp.39015048750940')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 75:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_009', '75.txt'))
        found = True
        break
if not found:
    print('Missing page 75 in volume pst.000006235918')
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 76:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_009', '76.txt'))
        found = True
        break
if not found:
    print('Missing page 76 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024796545_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015024796545')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 30:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015024796545_007', '30.txt'))
        found = True
        break
if not found:
    print('Missing page 30 in volume mdp.39015024796545')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_068'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.hn1nyx')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 147:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.hn1nyx_068', '147.txt'))
        found = True
        break
if not found:
    print('Missing page 147 in volume hvd.hn1nyx')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015042085947_037'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 66:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015042085947_037', '66.txt'))
        found = True
        break
if not found:
    print('Missing page 66 in volume mdp.39015042085947')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015042085947')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 67:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015042085947_037', '67.txt'))
        found = True
        break
if not found:
    print('Missing page 67 in volume mdp.39015042085947')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034262819_010'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034262819')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034262819_010', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume mdp.39015034262819')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015034262819')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 40:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034262819_010', '40.txt'))
        found = True
        break
if not found:
    print('Missing page 40 in volume mdp.39015034262819')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001132199_018'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001132199')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 43:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010001132199_018', '43.txt'))
        found = True
        break
if not found:
    print('Missing page 43 in volume emu.010001132199')
volume_dir = os.path.join(VOLUME_DIR, 'emu.010001132199')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 44:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010001132199_018', '44.txt'))
        found = True
        break
if not found:
    print('Missing page 44 in volume emu.010001132199')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_037'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 72:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015084107047_037', '72.txt'))
        found = True
        break
if not found:
    print('Missing page 72 in volume mdp.39015084107047')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 73:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015084107047_037', '73.txt'))
        found = True
        break
if not found:
    print('Missing page 73 in volume mdp.39015084107047')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_065'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 127:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_065', '127.txt'))
        found = True
        break
if not found:
    print('Missing page 127 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041016018_018'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041016018')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 88:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041016018_018', '88.txt'))
        found = True
        break
if not found:
    print('Missing page 88 in volume mdp.39015041016018')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041016018')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 89:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041016018_018', '89.txt'))
        found = True
        break
if not found:
    print('Missing page 89 in volume mdp.39015041016018')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015041016018')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 90:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041016018_018', '90.txt'))
        found = True
        break
if not found:
    print('Missing page 90 in volume mdp.39015041016018')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_027'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078774927_027', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume mdp.39015078774927')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015078774927')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 58:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078774927_027', '58.txt'))
        found = True
        break
if not found:
    print('Missing page 58 in volume mdp.39015078774927')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.49015001462457_003'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.49015001462457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 21:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_003', '21.txt'))
        found = True
        break
if not found:
    print('Missing page 21 in volume mdp.49015001462457')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.49015001462457')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 22:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_003', '22.txt'))
        found = True
        break
if not found:
    print('Missing page 22 in volume mdp.49015001462457')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056441465_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056441465')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 29:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056441465_015', '29.txt'))
        found = True
        break
if not found:
    print('Missing page 29 in volume mdp.39015056441465')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058068860_014'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 33:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058068860_014', '33.txt'))
        found = True
        break
if not found:
    print('Missing page 33 in volume mdp.39015058068860')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015058068860')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 34:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058068860_014', '34.txt'))
        found = True
        break
if not found:
    print('Missing page 34 in volume mdp.39015058068860')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_016'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 47:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_016', '47.txt'))
        found = True
        break
if not found:
    print('Missing page 47 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_053'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 91:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_053', '91.txt'))
        found = True
        break
if not found:
    print('Missing page 91 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044134446327_017'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044134446327')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044134446327_017', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume hvd.32044134446327')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044134446327')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 40:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044134446327_017', '40.txt'))
        found = True
        break
if not found:
    print('Missing page 40 in volume hvd.32044134446327')
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044134446327')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 41:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044134446327_017', '41.txt'))
        found = True
        break
if not found:
    print('Missing page 41 in volume hvd.32044134446327')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 53:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '53.txt'))
        found = True
        break
if not found:
    print('Missing page 53 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 54:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '54.txt'))
        found = True
        break
if not found:
    print('Missing page 54 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 55:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '55.txt'))
        found = True
        break
if not found:
    print('Missing page 55 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 58:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '58.txt'))
        found = True
        break
if not found:
    print('Missing page 58 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 59:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '59.txt'))
        found = True
        break
if not found:
    print('Missing page 59 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 60:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '60.txt'))
        found = True
        break
if not found:
    print('Missing page 60 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 61:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '61.txt'))
        found = True
        break
if not found:
    print('Missing page 61 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 62:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '62.txt'))
        found = True
        break
if not found:
    print('Missing page 62 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 63:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '63.txt'))
        found = True
        break
if not found:
    print('Missing page 63 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 64:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_003', '64.txt'))
        found = True
        break
if not found:
    print('Missing page 64 in volume mdp.39015010733783')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015031230439_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015031230439')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 8:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015031230439_004', '8.txt'))
        found = True
        break
if not found:
    print('Missing page 8 in volume mdp.39015031230439')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_010'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015084107047')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 26:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015084107047_010', '26.txt'))
        found = True
        break
if not found:
    print('Missing page 26 in volume mdp.39015084107047')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_024'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'hvd.32044050812528')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 106:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044050812528_024', '106.txt'))
        found = True
        break
if not found:
    print('Missing page 106 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_057'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 163:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_057', '163.txt'))
        found = True
        break
if not found:
    print('Missing page 163 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 14:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '14.txt'))
        found = True
        break
if not found:
    print('Missing page 14 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 15:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '15.txt'))
        found = True
        break
if not found:
    print('Missing page 15 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 16:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '16.txt'))
        found = True
        break
if not found:
    print('Missing page 16 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 17:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '17.txt'))
        found = True
        break
if not found:
    print('Missing page 17 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 18:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '18.txt'))
        found = True
        break
if not found:
    print('Missing page 18 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 19:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '19.txt'))
        found = True
        break
if not found:
    print('Missing page 19 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 20:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '20.txt'))
        found = True
        break
if not found:
    print('Missing page 20 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 21:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '21.txt'))
        found = True
        break
if not found:
    print('Missing page 21 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 22:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '22.txt'))
        found = True
        break
if not found:
    print('Missing page 22 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 23:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '23.txt'))
        found = True
        break
if not found:
    print('Missing page 23 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 25:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '25.txt'))
        found = True
        break
if not found:
    print('Missing page 25 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 26:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '26.txt'))
        found = True
        break
if not found:
    print('Missing page 26 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 27:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '27.txt'))
        found = True
        break
if not found:
    print('Missing page 27 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 28:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '28.txt'))
        found = True
        break
if not found:
    print('Missing page 28 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 29:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '29.txt'))
        found = True
        break
if not found:
    print('Missing page 29 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 30:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '30.txt'))
        found = True
        break
if not found:
    print('Missing page 30 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015063268315')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015063268315')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 32:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015063268315_002', '32.txt'))
        found = True
        break
if not found:
    print('Missing page 32 in volume mdp.39015063268315')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056944013_004'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056944013')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 19:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056944013_004', '19.txt'))
        found = True
        break
if not found:
    print('Missing page 19 in volume mdp.39015056944013')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032762174_009'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 32:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015032762174_009', '32.txt'))
        found = True
        break
if not found:
    print('Missing page 32 in volume mdp.39015032762174')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015031230439_001'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015031230439')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 5:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015031230439_001', '5.txt'))
        found = True
        break
if not found:
    print('Missing page 5 in volume mdp.39015031230439')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111037739_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000111037739')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 18:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000111037739_006', '18.txt'))
        found = True
        break
if not found:
    print('Missing page 18 in volume inu.30000111037739')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_014'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'umn.31951d02915219o')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 45:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_014', '45.txt'))
        found = True
        break
if not found:
    print('Missing page 45 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_005'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015040135538_005', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015040135538')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015059119985_030'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015059119985')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 61:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015059119985_030', '61.txt'))
        found = True
        break
if not found:
    print('Missing page 61 in volume mdp.39015059119985')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015059119985')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 62:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015059119985_030', '62.txt'))
        found = True
        break
if not found:
    print('Missing page 62 in volume mdp.39015059119985')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_030'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 72:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000107605259_030', '72.txt'))
        found = True
        break
if not found:
    print('Missing page 72 in volume inu.30000107605259')
volume_dir = os.path.join(VOLUME_DIR, 'inu.30000107605259')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 73:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000107605259_030', '73.txt'))
        found = True
        break
if not found:
    print('Missing page 73 in volume inu.30000107605259')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_045'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'pst.000006235918')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 141:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_045', '141.txt'))
        found = True
        break
if not found:
    print('Missing page 141 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056944013_014'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056944013')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 34:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056944013_014', '34.txt'))
        found = True
        break
if not found:
    print('Missing page 34 in volume mdp.39015056944013')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015056944013')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 35:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056944013_014', '35.txt'))
        found = True
        break
if not found:
    print('Missing page 35 in volume mdp.39015056944013')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015000252448_008'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015000252448')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 55:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015000252448_008', '55.txt'))
        found = True
        break
if not found:
    print('Missing page 55 in volume mdp.39015000252448')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_007'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'emu.010000709155')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010000709155_007', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume emu.010000709155')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.$b704626_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.$b704626')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 60:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.$b704626_015', '60.txt'))
        found = True
        break
if not found:
    print('Missing page 60 in volume uc1.$b704626')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 47:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '47.txt'))
        found = True
        break
if not found:
    print('Missing page 47 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 48:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '48.txt'))
        found = True
        break
if not found:
    print('Missing page 48 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 49:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '49.txt'))
        found = True
        break
if not found:
    print('Missing page 49 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 50:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '50.txt'))
        found = True
        break
if not found:
    print('Missing page 50 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 51:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_006', '51.txt'))
        found = True
        break
if not found:
    print('Missing page 51 in volume mdp.39015062571636')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019144424_028'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 64:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019144424_028', '64.txt'))
        found = True
        break
if not found:
    print('Missing page 64 in volume uc1.32106019144424')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 65:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019144424_028', '65.txt'))
        found = True
        break
if not found:
    print('Missing page 65 in volume uc1.32106019144424')
volume_dir = os.path.join(VOLUME_DIR, 'uc1.32106019144424')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 66:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019144424_028', '66.txt'))
        found = True
        break
if not found:
    print('Missing page 66 in volume uc1.32106019144424')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_059'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 97:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_059', '97.txt'))
        found = True
        break
if not found:
    print('Missing page 97 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037759605_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 47:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037759605_006', '47.txt'))
        found = True
        break
if not found:
    print('Missing page 47 in volume mdp.39015037759605')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 48:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037759605_006', '48.txt'))
        found = True
        break
if not found:
    print('Missing page 48 in volume mdp.39015037759605')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 49:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037759605_006', '49.txt'))
        found = True
        break
if not found:
    print('Missing page 49 in volume mdp.39015037759605')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015037759605')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 50:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037759605_006', '50.txt'))
        found = True
        break
if not found:
    print('Missing page 50 in volume mdp.39015037759605')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_043'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015040135538')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 103:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015040135538_043', '103.txt'))
        found = True
        break
if not found:
    print('Missing page 103 in volume mdp.39015040135538')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032762174_016'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 44:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015032762174_016', '44.txt'))
        found = True
        break
if not found:
    print('Missing page 44 in volume mdp.39015032762174')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 45:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015032762174_016', '45.txt'))
        found = True
        break
if not found:
    print('Missing page 45 in volume mdp.39015032762174')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015003918763_038'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015003918763')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 127:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015003918763_038', '127.txt'))
        found = True
        break
if not found:
    print('Missing page 127 in volume mdp.39015003918763')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 201:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '201.txt'))
        found = True
        break
if not found:
    print('Missing page 201 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 202:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '202.txt'))
        found = True
        break
if not found:
    print('Missing page 202 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 203:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '203.txt'))
        found = True
        break
if not found:
    print('Missing page 203 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 204:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '204.txt'))
        found = True
        break
if not found:
    print('Missing page 204 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 205:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '205.txt'))
        found = True
        break
if not found:
    print('Missing page 205 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 206:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '206.txt'))
        found = True
        break
if not found:
    print('Missing page 206 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 207:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '207.txt'))
        found = True
        break
if not found:
    print('Missing page 207 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 208:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '208.txt'))
        found = True
        break
if not found:
    print('Missing page 208 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 209:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '209.txt'))
        found = True
        break
if not found:
    print('Missing page 209 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 210:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '210.txt'))
        found = True
        break
if not found:
    print('Missing page 210 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 211:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '211.txt'))
        found = True
        break
if not found:
    print('Missing page 211 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 212:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '212.txt'))
        found = True
        break
if not found:
    print('Missing page 212 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 213:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '213.txt'))
        found = True
        break
if not found:
    print('Missing page 213 in volume mdp.39015062571636')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015062571636')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 214:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015062571636_022', '214.txt'))
        found = True
        break
if not found:
    print('Missing page 214 in volume mdp.39015062571636')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 233:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028', '233.txt'))
        found = True
        break
if not found:
    print('Missing page 233 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 234:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028', '234.txt'))
        found = True
        break
if not found:
    print('Missing page 234 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 235:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028', '235.txt'))
        found = True
        break
if not found:
    print('Missing page 235 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 236:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028', '236.txt'))
        found = True
        break
if not found:
    print('Missing page 236 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 237:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028', '237.txt'))
        found = True
        break
if not found:
    print('Missing page 237 in volume mdp.39015010733783')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015010733783')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 238:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015010733783_028', '238.txt'))
        found = True
        break
if not found:
    print('Missing page 238 in volume mdp.39015010733783')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_006'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 23:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_006', '23.txt'))
        found = True
        break
if not found:
    print('Missing page 23 in volume dul1.ark_13960_s2st3fdcwc7')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048915881_018'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_018', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_018', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume mdp.39015048915881')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015048915881')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 58:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048915881_018', '58.txt'))
        found = True
        break
if not found:
    print('Missing page 58 in volume mdp.39015048915881')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_021'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015029858522')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 45:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015029858522_021', '45.txt'))
        found = True
        break
if not found:
    print('Missing page 45 in volume mdp.39015029858522')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_034'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015038896729')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 81:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015038896729_034', '81.txt'))
        found = True
        break
if not found:
    print('Missing page 81 in volume mdp.39015038896729')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032762174_015'), exist_ok=True)
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 42:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015032762174_015', '42.txt'))
        found = True
        break
if not found:
    print('Missing page 42 in volume mdp.39015032762174')
volume_dir = os.path.join(VOLUME_DIR, 'mdp.39015032762174')
if not os.path.isdir(volume_dir):
    print('No such file or directory:', volume_dir)
    continue
found = False
for fname in os.listdir(volume_dir):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 43:
        src = os.path.join(volume_dir, fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015032762174_015', '43.txt'))
        found = True
        break
if not found:
    print('Missing page 43 in volume mdp.39015032762174')
