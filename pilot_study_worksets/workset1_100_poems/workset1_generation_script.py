import os
import shutil

VOLUME_DIR = 'Volumes'
OUTPUT_DIR = os.path.join('MyPoemAssignments', 'Collection')
os.makedirs(OUTPUT_DIR, exist_ok=True)

os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_007'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 26:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_007', '26.txt'))
        found = True
        break
if not found:
    print('Missing page 26 in volume mdp.39015021471480')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 27:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_007', '27.txt'))
        found = True
        break
if not found:
    print('Missing page 27 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069332370_030'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015069332370')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 69:
        src = os.path.join(VOLUME_DIR, 'mdp.39015069332370', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015069332370_030', '69.txt'))
        found = True
        break
if not found:
    print('Missing page 69 in volume mdp.39015069332370')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015048918893_010'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015048918893')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 29:
        src = os.path.join(VOLUME_DIR, 'mdp.39015048918893', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015048918893_010', '29.txt'))
        found = True
        break
if not found:
    print('Missing page 29 in volume mdp.39015048918893')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010000709155_056'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'emu.010000709155')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 97:
        src = os.path.join(VOLUME_DIR, 'emu.010000709155', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010000709155_056', '97.txt'))
        found = True
        break
if not found:
    print('Missing page 97 in volume emu.010000709155')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106007406611_019'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106007406611')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 54:
        src = os.path.join(VOLUME_DIR, 'uc1.32106007406611', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106007406611_019', '54.txt'))
        found = True
        break
if not found:
    print('Missing page 54 in volume uc1.32106007406611')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034908049_022'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015034908049')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 105:
        src = os.path.join(VOLUME_DIR, 'mdp.39015034908049', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034908049_022', '105.txt'))
        found = True
        break
if not found:
    print('Missing page 105 in volume mdp.39015034908049')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_008'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'hvd.32044050812528')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 87:
        src = os.path.join(VOLUME_DIR, 'hvd.32044050812528', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044050812528_008', '87.txt'))
        found = True
        break
if not found:
    print('Missing page 87 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054448207_020'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054448207')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 66:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054448207', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054448207_020', '66.txt'))
        found = True
        break
if not found:
    print('Missing page 66 in volume mdp.39015054448207')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054448207')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 67:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054448207', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054448207_020', '67.txt'))
        found = True
        break
if not found:
    print('Missing page 67 in volume mdp.39015054448207')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024695457_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015024695457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 16:
        src = os.path.join(VOLUME_DIR, 'mdp.39015024695457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015024695457_004', '16.txt'))
        found = True
        break
if not found:
    print('Missing page 16 in volume mdp.39015024695457')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_018'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'hvd.32044080899966')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 38:
        src = os.path.join(VOLUME_DIR, 'hvd.32044080899966', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044080899966_018', '38.txt'))
        found = True
        break
if not found:
    print('Missing page 38 in volume hvd.32044080899966')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054273282_009'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054273282')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054273282', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054273282_009', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume mdp.39015054273282')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_034'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106019480612')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 80:
        src = os.path.join(VOLUME_DIR, 'uc1.32106019480612', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019480612_034', '80.txt'))
        found = True
        break
if not found:
    print('Missing page 80 in volume uc1.32106019480612')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106019480612')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 81:
        src = os.path.join(VOLUME_DIR, 'uc1.32106019480612', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019480612_034', '81.txt'))
        found = True
        break
if not found:
    print('Missing page 81 in volume uc1.32106019480612')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 93:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '93.txt'))
        found = True
        break
if not found:
    print('Missing page 93 in volume mdp.49015001462457')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 94:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '94.txt'))
        found = True
        break
if not found:
    print('Missing page 94 in volume mdp.49015001462457')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 95:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '95.txt'))
        found = True
        break
if not found:
    print('Missing page 95 in volume mdp.49015001462457')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 96:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '96.txt'))
        found = True
        break
if not found:
    print('Missing page 96 in volume mdp.49015001462457')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 97:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '97.txt'))
        found = True
        break
if not found:
    print('Missing page 97 in volume mdp.49015001462457')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 98:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '98.txt'))
        found = True
        break
if not found:
    print('Missing page 98 in volume mdp.49015001462457')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.49015001462457')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 99:
        src = os.path.join(VOLUME_DIR, 'mdp.49015001462457', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.49015001462457_030', '99.txt'))
        found = True
        break
if not found:
    print('Missing page 99 in volume mdp.49015001462457')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_016'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 55:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_016', '55.txt'))
        found = True
        break
if not found:
    print('Missing page 55 in volume dul1.ark_13960_s2st3fdcwc7')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_016', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume dul1.ark_13960_s2st3fdcwc7')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_016', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume dul1.ark_13960_s2st3fdcwc7')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 58:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_s2st3fdcwc7', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_s2st3fdcwc7_016', '58.txt'))
        found = True
        break
if not found:
    print('Missing page 58 in volume dul1.ark_13960_s2st3fdcwc7')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106007406611_038'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106007406611')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 85:
        src = os.path.join(VOLUME_DIR, 'uc1.32106007406611', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106007406611_038', '85.txt'))
        found = True
        break
if not found:
    print('Missing page 85 in volume uc1.32106007406611')
os.makedirs(os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_012'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uiuc.99685572812205899')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 42:
        src = os.path.join(VOLUME_DIR, 'uiuc.99685572812205899', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_012', '42.txt'))
        found = True
        break
if not found:
    print('Missing page 42 in volume uiuc.99685572812205899')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_060'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 98:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_060', '98.txt'))
        found = True
        break
if not found:
    print('Missing page 98 in volume dul1.ark_13960_t27b3zv3b')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 99:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_060', '99.txt'))
        found = True
        break
if not found:
    print('Missing page 99 in volume dul1.ark_13960_t27b3zv3b')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 100:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_060', '100.txt'))
        found = True
        break
if not found:
    print('Missing page 100 in volume dul1.ark_13960_t27b3zv3b')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 101:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_060', '101.txt'))
        found = True
        break
if not found:
    print('Missing page 101 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015043788846_008'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015043788846')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(VOLUME_DIR, 'mdp.39015043788846', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015043788846_008', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015043788846')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037819169_015'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015037819169')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 60:
        src = os.path.join(VOLUME_DIR, 'mdp.39015037819169', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037819169_015', '60.txt'))
        found = True
        break
if not found:
    print('Missing page 60 in volume mdp.39015037819169')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_026'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 51:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t3f00205w', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t3f00205w_026', '51.txt'))
        found = True
        break
if not found:
    print('Missing page 51 in volume dul1.ark_13960_t3f00205w')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_021'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 51:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_021', '51.txt'))
        found = True
        break
if not found:
    print('Missing page 51 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000068225810_034'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'pst.000068225810')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 68:
        src = os.path.join(VOLUME_DIR, 'pst.000068225810', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000068225810_034', '68.txt'))
        found = True
        break
if not found:
    print('Missing page 68 in volume pst.000068225810')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'pst.000068225810')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 69:
        src = os.path.join(VOLUME_DIR, 'pst.000068225810', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000068225810_034', '69.txt'))
        found = True
        break
if not found:
    print('Missing page 69 in volume pst.000068225810')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'pst.000068225810')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 70:
        src = os.path.join(VOLUME_DIR, 'pst.000068225810', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000068225810_034', '70.txt'))
        found = True
        break
if not found:
    print('Missing page 70 in volume pst.000068225810')
os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173010198907_044'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'txu.059173010198907')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 92:
        src = os.path.join(VOLUME_DIR, 'txu.059173010198907', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173010198907_044', '92.txt'))
        found = True
        break
if not found:
    print('Missing page 92 in volume txu.059173010198907')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058066179_011'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058066179')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 38:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058066179', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058066179_011', '38.txt'))
        found = True
        break
if not found:
    print('Missing page 38 in volume mdp.39015058066179')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058066179')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058066179', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058066179_011', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume mdp.39015058066179')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060020230_039'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015060020230')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 74:
        src = os.path.join(VOLUME_DIR, 'mdp.39015060020230', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060020230_039', '74.txt'))
        found = True
        break
if not found:
    print('Missing page 74 in volume mdp.39015060020230')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040135538_088'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015040135538')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 180:
        src = os.path.join(VOLUME_DIR, 'mdp.39015040135538', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015040135538_088', '180.txt'))
        found = True
        break
if not found:
    print('Missing page 180 in volume mdp.39015040135538')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060820183_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015060820183')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(VOLUME_DIR, 'mdp.39015060820183', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060820183_004', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume mdp.39015060820183')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015060820183')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 25:
        src = os.path.join(VOLUME_DIR, 'mdp.39015060820183', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060820183_004', '25.txt'))
        found = True
        break
if not found:
    print('Missing page 25 in volume mdp.39015060820183')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015060820183')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 26:
        src = os.path.join(VOLUME_DIR, 'mdp.39015060820183', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060820183_004', '26.txt'))
        found = True
        break
if not found:
    print('Missing page 26 in volume mdp.39015060820183')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015060820183')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 27:
        src = os.path.join(VOLUME_DIR, 'mdp.39015060820183', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060820183_004', '27.txt'))
        found = True
        break
if not found:
    print('Missing page 27 in volume mdp.39015060820183')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_071'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'umn.31951d02915219o')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 139:
        src = os.path.join(VOLUME_DIR, 'umn.31951d02915219o', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_071', '139.txt'))
        found = True
        break
if not found:
    print('Missing page 139 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054303139_039'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054303139')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 80:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054303139', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054303139_039', '80.txt'))
        found = True
        break
if not found:
    print('Missing page 80 in volume mdp.39015054303139')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054303139')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 81:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054303139', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054303139_039', '81.txt'))
        found = True
        break
if not found:
    print('Missing page 81 in volume mdp.39015054303139')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015069361874_020'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015069361874')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 48:
        src = os.path.join(VOLUME_DIR, 'mdp.39015069361874', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015069361874_020', '48.txt'))
        found = True
        break
if not found:
    print('Missing page 48 in volume mdp.39015069361874')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015069361874')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 49:
        src = os.path.join(VOLUME_DIR, 'mdp.39015069361874', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015069361874_020', '49.txt'))
        found = True
        break
if not found:
    print('Missing page 49 in volume mdp.39015069361874')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015073926746_007'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015073926746')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 23:
        src = os.path.join(VOLUME_DIR, 'mdp.39015073926746', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015073926746_007', '23.txt'))
        found = True
        break
if not found:
    print('Missing page 23 in volume mdp.39015073926746')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_003'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058271480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 18:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058271480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058271480_003', '18.txt'))
        found = True
        break
if not found:
    print('Missing page 18 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_022'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 107:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_022', '107.txt'))
        found = True
        break
if not found:
    print('Missing page 107 in volume loc.ark_13960_t4pk0ws6x')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 108:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_022', '108.txt'))
        found = True
        break
if not found:
    print('Missing page 108 in volume loc.ark_13960_t4pk0ws6x')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 109:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_022', '109.txt'))
        found = True
        break
if not found:
    print('Missing page 109 in volume loc.ark_13960_t4pk0ws6x')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 110:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t4pk0ws6x', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t4pk0ws6x_022', '110.txt'))
        found = True
        break
if not found:
    print('Missing page 110 in volume loc.ark_13960_t4pk0ws6x')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015019441578')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 76:
        src = os.path.join(VOLUME_DIR, 'mdp.39015019441578', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015', '76.txt'))
        found = True
        break
if not found:
    print('Missing page 76 in volume mdp.39015019441578')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015019441578')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 77:
        src = os.path.join(VOLUME_DIR, 'mdp.39015019441578', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015', '77.txt'))
        found = True
        break
if not found:
    print('Missing page 77 in volume mdp.39015019441578')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015019441578')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 78:
        src = os.path.join(VOLUME_DIR, 'mdp.39015019441578', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015019441578_015', '78.txt'))
        found = True
        break
if not found:
    print('Missing page 78 in volume mdp.39015019441578')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015037873620_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015037873620')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 28:
        src = os.path.join(VOLUME_DIR, 'mdp.39015037873620', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037873620_004', '28.txt'))
        found = True
        break
if not found:
    print('Missing page 28 in volume mdp.39015037873620')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015037873620')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 29:
        src = os.path.join(VOLUME_DIR, 'mdp.39015037873620', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015037873620_004', '29.txt'))
        found = True
        break
if not found:
    print('Missing page 29 in volume mdp.39015037873620')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_007'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015008570940')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 43:
        src = os.path.join(VOLUME_DIR, 'mdp.39015008570940', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015008570940_007', '43.txt'))
        found = True
        break
if not found:
    print('Missing page 43 in volume mdp.39015008570940')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_018'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 47:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_018', '47.txt'))
        found = True
        break
if not found:
    print('Missing page 47 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000111037739_003'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'inu.30000111037739')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 15:
        src = os.path.join(VOLUME_DIR, 'inu.30000111037739', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000111037739_003', '15.txt'))
        found = True
        break
if not found:
    print('Missing page 15 in volume inu.30000111037739')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_040'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'pst.000006235918')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 131:
        src = os.path.join(VOLUME_DIR, 'pst.000006235918', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_040', '131.txt'))
        found = True
        break
if not found:
    print('Missing page 131 in volume pst.000006235918')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'pst.000006235918')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 132:
        src = os.path.join(VOLUME_DIR, 'pst.000006235918', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_040', '132.txt'))
        found = True
        break
if not found:
    print('Missing page 132 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015029858522_042'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015029858522')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 66:
        src = os.path.join(VOLUME_DIR, 'mdp.39015029858522', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015029858522_042', '66.txt'))
        found = True
        break
if not found:
    print('Missing page 66 in volume mdp.39015029858522')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078788448')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 101:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078788448', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031', '101.txt'))
        found = True
        break
if not found:
    print('Missing page 101 in volume mdp.39015078788448')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078788448')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 102:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078788448', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031', '102.txt'))
        found = True
        break
if not found:
    print('Missing page 102 in volume mdp.39015078788448')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078788448')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 103:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078788448', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078788448_031', '103.txt'))
        found = True
        break
if not found:
    print('Missing page 103 in volume mdp.39015078788448')
os.makedirs(os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_057'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 127:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_057', '127.txt'))
        found = True
        break
if not found:
    print('Missing page 127 in volume loc.ark_13960_t1ng55d1m')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 128:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_057', '128.txt'))
        found = True
        break
if not found:
    print('Missing page 128 in volume loc.ark_13960_t1ng55d1m')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 129:
        src = os.path.join(VOLUME_DIR, 'loc.ark_13960_t1ng55d1m', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'loc.ark_13960_t1ng55d1m_057', '129.txt'))
        found = True
        break
if not found:
    print('Missing page 129 in volume loc.ark_13960_t1ng55d1m')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_053'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078805275')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 140:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078805275', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078805275_053', '140.txt'))
        found = True
        break
if not found:
    print('Missing page 140 in volume mdp.39015078805275')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.$b704626_011'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.$b704626')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 52:
        src = os.path.join(VOLUME_DIR, 'uc1.$b704626', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.$b704626_011', '52.txt'))
        found = True
        break
if not found:
    print('Missing page 52 in volume uc1.$b704626')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.$b704626')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 53:
        src = os.path.join(VOLUME_DIR, 'uc1.$b704626', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.$b704626_011', '53.txt'))
        found = True
        break
if not found:
    print('Missing page 53 in volume uc1.$b704626')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015013350502_021'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 75:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_021', '75.txt'))
        found = True
        break
if not found:
    print('Missing page 75 in volume mdp.39015013350502')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 76:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_021', '76.txt'))
        found = True
        break
if not found:
    print('Missing page 76 in volume mdp.39015013350502')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 77:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_021', '77.txt'))
        found = True
        break
if not found:
    print('Missing page 77 in volume mdp.39015013350502')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015040730916_024'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015040730916')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 59:
        src = os.path.join(VOLUME_DIR, 'mdp.39015040730916', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015040730916_024', '59.txt'))
        found = True
        break
if not found:
    print('Missing page 59 in volume mdp.39015040730916')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_044'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078805275')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 127:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078805275', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078805275_044', '127.txt'))
        found = True
        break
if not found:
    print('Missing page 127 in volume mdp.39015078805275')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078805275')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 128:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078805275', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078805275_044', '128.txt'))
        found = True
        break
if not found:
    print('Missing page 128 in volume mdp.39015078805275')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_014'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015008570940')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(VOLUME_DIR, 'mdp.39015008570940', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015008570940_014', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume mdp.39015008570940')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015008570940')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(VOLUME_DIR, 'mdp.39015008570940', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015008570940_014', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume mdp.39015008570940')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015024796545_003'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015024796545')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(VOLUME_DIR, 'mdp.39015024796545', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015024796545_003', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume mdp.39015024796545')
os.makedirs(os.path.join(OUTPUT_DIR, 'emu.010001132199_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'emu.010001132199')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 18:
        src = os.path.join(VOLUME_DIR, 'emu.010001132199', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'emu.010001132199_004', '18.txt'))
        found = True
        break
if not found:
    print('Missing page 18 in volume emu.010001132199')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_051'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 87:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_051', '87.txt'))
        found = True
        break
if not found:
    print('Missing page 87 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041016018_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015041016018')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(VOLUME_DIR, 'mdp.39015041016018', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041016018_004', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume mdp.39015041016018')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015041016018')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 25:
        src = os.path.join(VOLUME_DIR, 'mdp.39015041016018', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041016018_004', '25.txt'))
        found = True
        break
if not found:
    print('Missing page 25 in volume mdp.39015041016018')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015008570940_036'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015008570940')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 100:
        src = os.path.join(VOLUME_DIR, 'mdp.39015008570940', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015008570940_036', '100.txt'))
        found = True
        break
if not found:
    print('Missing page 100 in volume mdp.39015008570940')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_028'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 64:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_028', '64.txt'))
        found = True
        break
if not found:
    print('Missing page 64 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015032504220_028'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015032504220')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 70:
        src = os.path.join(VOLUME_DIR, 'mdp.39015032504220', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015032504220_028', '70.txt'))
        found = True
        break
if not found:
    print('Missing page 70 in volume mdp.39015032504220')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078774927')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 22:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078774927', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078774927_004', '22.txt'))
        found = True
        break
if not found:
    print('Missing page 22 in volume mdp.39015078774927')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056441465_023'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015056441465')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 42:
        src = os.path.join(VOLUME_DIR, 'mdp.39015056441465', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056441465_023', '42.txt'))
        found = True
        break
if not found:
    print('Missing page 42 in volume mdp.39015056441465')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015056441465')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 43:
        src = os.path.join(VOLUME_DIR, 'mdp.39015056441465', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056441465_023', '43.txt'))
        found = True
        break
if not found:
    print('Missing page 43 in volume mdp.39015056441465')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015028916677_024'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015028916677')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 52:
        src = os.path.join(VOLUME_DIR, 'mdp.39015028916677', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015028916677_024', '52.txt'))
        found = True
        break
if not found:
    print('Missing page 52 in volume mdp.39015028916677')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015028916677')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 53:
        src = os.path.join(VOLUME_DIR, 'mdp.39015028916677', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015028916677_024', '53.txt'))
        found = True
        break
if not found:
    print('Missing page 53 in volume mdp.39015028916677')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_025'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_025', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume mdp.39015021471480')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_025', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'pst.000006235918_069'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'pst.000006235918')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 184:
        src = os.path.join(VOLUME_DIR, 'pst.000006235918', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'pst.000006235918_069', '184.txt'))
        found = True
        break
if not found:
    print('Missing page 184 in volume pst.000006235918')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015046852540_033'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015046852540')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 95:
        src = os.path.join(VOLUME_DIR, 'mdp.39015046852540', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015046852540_033', '95.txt'))
        found = True
        break
if not found:
    print('Missing page 95 in volume mdp.39015046852540')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015046852540')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 96:
        src = os.path.join(VOLUME_DIR, 'mdp.39015046852540', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015046852540_033', '96.txt'))
        found = True
        break
if not found:
    print('Missing page 96 in volume mdp.39015046852540')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058066179_008'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058066179')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 34:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058066179', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058066179_008', '34.txt'))
        found = True
        break
if not found:
    print('Missing page 34 in volume mdp.39015058066179')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034259393_001'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015034259393')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 21:
        src = os.path.join(VOLUME_DIR, 'mdp.39015034259393', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034259393_001', '21.txt'))
        found = True
        break
if not found:
    print('Missing page 21 in volume mdp.39015034259393')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015034259393')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 22:
        src = os.path.join(VOLUME_DIR, 'mdp.39015034259393', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034259393_001', '22.txt'))
        found = True
        break
if not found:
    print('Missing page 22 in volume mdp.39015034259393')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044050812528_070'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'hvd.32044050812528')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 164:
        src = os.path.join(VOLUME_DIR, 'hvd.32044050812528', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044050812528_070', '164.txt'))
        found = True
        break
if not found:
    print('Missing page 164 in volume hvd.32044050812528')
os.makedirs(os.path.join(OUTPUT_DIR, 'inu.30000107605259_041'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'inu.30000107605259')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 88:
        src = os.path.join(VOLUME_DIR, 'inu.30000107605259', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'inu.30000107605259_041', '88.txt'))
        found = True
        break
if not found:
    print('Missing page 88 in volume inu.30000107605259')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015038896729_016'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015038896729')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 63:
        src = os.path.join(VOLUME_DIR, 'mdp.39015038896729', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015038896729_016', '63.txt'))
        found = True
        break
if not found:
    print('Missing page 63 in volume mdp.39015038896729')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_048'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058271480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 74:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058271480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058271480_048', '74.txt'))
        found = True
        break
if not found:
    print('Missing page 74 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_005'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'umn.31951d02915219o')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 33:
        src = os.path.join(VOLUME_DIR, 'umn.31951d02915219o', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'umn.31951d02915219o_005', '33.txt'))
        found = True
        break
if not found:
    print('Missing page 33 in volume umn.31951d02915219o')
os.makedirs(os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_008'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 24:
        src = os.path.join(VOLUME_DIR, 'dul1.ark_13960_t27b3zv3b', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'dul1.ark_13960_t27b3zv3b_008', '24.txt'))
        found = True
        break
if not found:
    print('Missing page 24 in volume dul1.ark_13960_t27b3zv3b')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106007406611_003'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106007406611')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 22:
        src = os.path.join(VOLUME_DIR, 'uc1.32106007406611', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106007406611_003', '22.txt'))
        found = True
        break
if not found:
    print('Missing page 22 in volume uc1.32106007406611')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015056652319_013'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015056652319')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 47:
        src = os.path.join(VOLUME_DIR, 'mdp.39015056652319', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056652319_013', '47.txt'))
        found = True
        break
if not found:
    print('Missing page 47 in volume mdp.39015056652319')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015056652319')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 48:
        src = os.path.join(VOLUME_DIR, 'mdp.39015056652319', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015056652319_013', '48.txt'))
        found = True
        break
if not found:
    print('Missing page 48 in volume mdp.39015056652319')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078805275_048'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078805275')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 133:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078805275', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078805275_048', '133.txt'))
        found = True
        break
if not found:
    print('Missing page 133 in volume mdp.39015078805275')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106018768926_017'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106018768926')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 57:
        src = os.path.join(VOLUME_DIR, 'uc1.32106018768926', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106018768926_017', '57.txt'))
        found = True
        break
if not found:
    print('Missing page 57 in volume uc1.32106018768926')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_001'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058271480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 16:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058271480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058271480_001', '16.txt'))
        found = True
        break
if not found:
    print('Missing page 16 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015034262819_018'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015034262819')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 53:
        src = os.path.join(VOLUME_DIR, 'mdp.39015034262819', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034262819_018', '53.txt'))
        found = True
        break
if not found:
    print('Missing page 53 in volume mdp.39015034262819')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015034262819')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 54:
        src = os.path.join(VOLUME_DIR, 'mdp.39015034262819', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034262819_018', '54.txt'))
        found = True
        break
if not found:
    print('Missing page 54 in volume mdp.39015034262819')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015034262819')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 55:
        src = os.path.join(VOLUME_DIR, 'mdp.39015034262819', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015034262819_018', '55.txt'))
        found = True
        break
if not found:
    print('Missing page 55 in volume mdp.39015034262819')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015058271480_004'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015058271480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 19:
        src = os.path.join(VOLUME_DIR, 'mdp.39015058271480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015058271480_004', '19.txt'))
        found = True
        break
if not found:
    print('Missing page 19 in volume mdp.39015058271480')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015013350502_012'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 53:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_012', '53.txt'))
        found = True
        break
if not found:
    print('Missing page 53 in volume mdp.39015013350502')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 54:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_012', '54.txt'))
        found = True
        break
if not found:
    print('Missing page 54 in volume mdp.39015013350502')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 55:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_012', '55.txt'))
        found = True
        break
if not found:
    print('Missing page 55 in volume mdp.39015013350502')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015013350502')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 56:
        src = os.path.join(VOLUME_DIR, 'mdp.39015013350502', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015013350502_012', '56.txt'))
        found = True
        break
if not found:
    print('Missing page 56 in volume mdp.39015013350502')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041056824_037'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015041056824')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 62:
        src = os.path.join(VOLUME_DIR, 'mdp.39015041056824', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041056824_037', '62.txt'))
        found = True
        break
if not found:
    print('Missing page 62 in volume mdp.39015041056824')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015049644100_053'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015049644100')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 181:
        src = os.path.join(VOLUME_DIR, 'mdp.39015049644100', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015049644100_053', '181.txt'))
        found = True
        break
if not found:
    print('Missing page 181 in volume mdp.39015049644100')
os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_002'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 20:
        src = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_002', '20.txt'))
        found = True
        break
if not found:
    print('Missing page 20 in volume ucbk.ark_28722_h20g3h67c')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015041016018_010'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015041016018')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 61:
        src = os.path.join(VOLUME_DIR, 'mdp.39015041016018', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015041016018_010', '61.txt'))
        found = True
        break
if not found:
    print('Missing page 61 in volume mdp.39015041016018')
os.makedirs(os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_015'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 35:
        src = os.path.join(VOLUME_DIR, 'ucbk.ark_28722_h20g3h67c', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'ucbk.ark_28722_h20g3h67c_015', '35.txt'))
        found = True
        break
if not found:
    print('Missing page 35 in volume ucbk.ark_28722_h20g3h67c')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015059119985_013'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015059119985')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 33:
        src = os.path.join(VOLUME_DIR, 'mdp.39015059119985', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015059119985_013', '33.txt'))
        found = True
        break
if not found:
    print('Missing page 33 in volume mdp.39015059119985')
os.makedirs(os.path.join(OUTPUT_DIR, 'txu.059173010296815_002'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'txu.059173010296815')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 13:
        src = os.path.join(VOLUME_DIR, 'txu.059173010296815', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173010296815_002', '13.txt'))
        found = True
        break
if not found:
    print('Missing page 13 in volume txu.059173010296815')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'txu.059173010296815')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 14:
        src = os.path.join(VOLUME_DIR, 'txu.059173010296815', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'txu.059173010296815_002', '14.txt'))
        found = True
        break
if not found:
    print('Missing page 14 in volume txu.059173010296815')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015078774927_022'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015078774927')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 46:
        src = os.path.join(VOLUME_DIR, 'mdp.39015078774927', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015078774927_022', '46.txt'))
        found = True
        break
if not found:
    print('Missing page 46 in volume mdp.39015078774927')
os.makedirs(os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_029'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uiuc.99685572812205899')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 91:
        src = os.path.join(VOLUME_DIR, 'uiuc.99685572812205899', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_029', '91.txt'))
        found = True
        break
if not found:
    print('Missing page 91 in volume uiuc.99685572812205899')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uiuc.99685572812205899')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 92:
        src = os.path.join(VOLUME_DIR, 'uiuc.99685572812205899', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uiuc.99685572812205899_029', '92.txt'))
        found = True
        break
if not found:
    print('Missing page 92 in volume uiuc.99685572812205899')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015084107047_052'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015084107047')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 95:
        src = os.path.join(VOLUME_DIR, 'mdp.39015084107047', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015084107047_052', '95.txt'))
        found = True
        break
if not found:
    print('Missing page 95 in volume mdp.39015084107047')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_019'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'hvd.32044080899966')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(VOLUME_DIR, 'hvd.32044080899966', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044080899966_019', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume hvd.32044080899966')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106007406611_010'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106007406611')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 39:
        src = os.path.join(VOLUME_DIR, 'uc1.32106007406611', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106007406611_010', '39.txt'))
        found = True
        break
if not found:
    print('Missing page 39 in volume uc1.32106007406611')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054303139_020'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054303139')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 38:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054303139', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054303139_020', '38.txt'))
        found = True
        break
if not found:
    print('Missing page 38 in volume mdp.39015054303139')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015055796364_002'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015055796364')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 25:
        src = os.path.join(VOLUME_DIR, 'mdp.39015055796364', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055796364_002', '25.txt'))
        found = True
        break
if not found:
    print('Missing page 25 in volume mdp.39015055796364')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015055796364')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 26:
        src = os.path.join(VOLUME_DIR, 'mdp.39015055796364', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015055796364_002', '26.txt'))
        found = True
        break
if not found:
    print('Missing page 26 in volume mdp.39015055796364')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015054448207_026'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015054448207')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 89:
        src = os.path.join(VOLUME_DIR, 'mdp.39015054448207', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015054448207_026', '89.txt'))
        found = True
        break
if not found:
    print('Missing page 89 in volume mdp.39015054448207')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015011313247_002'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015011313247')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 17:
        src = os.path.join(VOLUME_DIR, 'mdp.39015011313247', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015011313247_002', '17.txt'))
        found = True
        break
if not found:
    print('Missing page 17 in volume mdp.39015011313247')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_010'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015047858124')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 30:
        src = os.path.join(VOLUME_DIR, 'mdp.39015047858124', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_010', '30.txt'))
        found = True
        break
if not found:
    print('Missing page 30 in volume mdp.39015047858124')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015047858124')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 31:
        src = os.path.join(VOLUME_DIR, 'mdp.39015047858124', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_010', '31.txt'))
        found = True
        break
if not found:
    print('Missing page 31 in volume mdp.39015047858124')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015047858124')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 34:
        src = os.path.join(VOLUME_DIR, 'mdp.39015047858124', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012', '34.txt'))
        found = True
        break
if not found:
    print('Missing page 34 in volume mdp.39015047858124')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015047858124')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 35:
        src = os.path.join(VOLUME_DIR, 'mdp.39015047858124', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012', '35.txt'))
        found = True
        break
if not found:
    print('Missing page 35 in volume mdp.39015047858124')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015047858124')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 36:
        src = os.path.join(VOLUME_DIR, 'mdp.39015047858124', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015047858124_012', '36.txt'))
        found = True
        break
if not found:
    print('Missing page 36 in volume mdp.39015047858124')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015021471480_039'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 79:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_039', '79.txt'))
        found = True
        break
if not found:
    print('Missing page 79 in volume mdp.39015021471480')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015021471480')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 80:
        src = os.path.join(VOLUME_DIR, 'mdp.39015021471480', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015021471480_039', '80.txt'))
        found = True
        break
if not found:
    print('Missing page 80 in volume mdp.39015021471480')
os.makedirs(os.path.join(OUTPUT_DIR, 'uc1.32106019480612_010'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106019480612')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 35:
        src = os.path.join(VOLUME_DIR, 'uc1.32106019480612', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019480612_010', '35.txt'))
        found = True
        break
if not found:
    print('Missing page 35 in volume uc1.32106019480612')
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'uc1.32106019480612')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 36:
        src = os.path.join(VOLUME_DIR, 'uc1.32106019480612', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'uc1.32106019480612_010', '36.txt'))
        found = True
        break
if not found:
    print('Missing page 36 in volume uc1.32106019480612')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015060820183_016'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015060820183')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 43:
        src = os.path.join(VOLUME_DIR, 'mdp.39015060820183', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015060820183_016', '43.txt'))
        found = True
        break
if not found:
    print('Missing page 43 in volume mdp.39015060820183')
os.makedirs(os.path.join(OUTPUT_DIR, 'hvd.32044080899966_007'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'hvd.32044080899966')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 25:
        src = os.path.join(VOLUME_DIR, 'hvd.32044080899966', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'hvd.32044080899966_007', '25.txt'))
        found = True
        break
if not found:
    print('Missing page 25 in volume hvd.32044080899966')
os.makedirs(os.path.join(OUTPUT_DIR, 'mdp.39015031230439_005'), exist_ok=True)
found = False
for fname in os.listdir(os.path.join(VOLUME_DIR, 'mdp.39015031230439')):
    base = fname.split('.')[0]
    try:
        page_num = int(base.lstrip('0') or '0')
    except ValueError:
        continue
    if page_num == 9:
        src = os.path.join(VOLUME_DIR, 'mdp.39015031230439', fname)
        shutil.copy(src, os.path.join(OUTPUT_DIR, 'mdp.39015031230439_005', '9.txt'))
        found = True
        break
if not found:
    print('Missing page 9 in volume mdp.39015031230439')
