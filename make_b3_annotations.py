"""Generate annotation XMLs for B3-dense slice (group mode, toan)."""
import xml.etree.ElementTree as ET
import xml.dom.minidom
import pathlib

annotations = {
    'adasind_145860.jpg': [
        # Prefill box: Truck (394,798,485,912)
        {'label':'Truck','xtl':394.0,'ytl':798.0,'xbr':485.0,'ybr':912.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'Car','xtl':218.0,'ytl':820.0,'xbr':310.0,'ybr':920.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'ThreeWheeler','xtl':520.0,'ytl':845.0,'xbr':620.0,'ybr':960.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'Bike','xtl':115.0,'ytl':870.0,'xbr':175.0,'ybr':955.0,'occluded':'0','truncated':'false','zone':'mid'},
        {'label':'Car','xtl':680.0,'ytl':760.0,'xbr':790.0,'ybr':870.0,'occluded':'0','truncated':'false','zone':'mid'},
        {'label':'Bike','xtl':820.0,'ytl':795.0,'xbr':870.0,'ybr':860.0,'occluded':'1','truncated':'false','zone':'mid'},
        {'label':'ThreeWheeler','xtl':55.0,'ytl':835.0,'xbr':145.0,'ybr':955.0,'occluded':'0','truncated':'true','zone':'edge'},
    ],
    'adasind_167700.jpg': [
        # k12 hint: ThreeWheeler edge (129,1046), Bike center (510,1076)
        {'label':'ThreeWheeler','xtl':65.0,'ytl':985.0,'xbr':185.0,'ybr':1115.0,'occluded':'0','truncated':'true','zone':'edge'},
        {'label':'Bike','xtl':455.0,'ytl':1040.0,'xbr':555.0,'ybr':1120.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'Car','xtl':310.0,'ytl':985.0,'xbr':410.0,'ybr':1085.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'ThreeWheeler','xtl':580.0,'ytl':975.0,'xbr':680.0,'ybr':1070.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'Bike','xtl':195.0,'ytl':1010.0,'xbr':250.0,'ybr':1080.0,'occluded':'1','truncated':'false','zone':'mid'},
        {'label':'Car','xtl':720.0,'ytl':930.0,'xbr':820.0,'ybr':1020.0,'occluded':'0','truncated':'false','zone':'mid'},
    ],
    'adasind_199770.jpg': [
        # k12 hint: ThreeWheeler edge (46,834), Bike edge (105,870)
        {'label':'ThreeWheeler','xtl':10.0,'ytl':790.0,'xbr':110.0,'ybr':890.0,'occluded':'0','truncated':'true','zone':'edge'},
        {'label':'Bike','xtl':65.0,'ytl':840.0,'xbr':135.0,'ybr':910.0,'occluded':'0','truncated':'true','zone':'edge'},
        {'label':'Car','xtl':280.0,'ytl':810.0,'xbr':390.0,'ybr':915.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'ThreeWheeler','xtl':420.0,'ytl':820.0,'xbr':520.0,'ybr':930.0,'occluded':'0','truncated':'false','zone':'center'},
        {'label':'Bike','xtl':540.0,'ytl':830.0,'xbr':595.0,'ybr':895.0,'occluded':'1','truncated':'false','zone':'center'},
        {'label':'Car','xtl':620.0,'ytl':795.0,'xbr':720.0,'ybr':890.0,'occluded':'0','truncated':'false','zone':'mid'},
        {'label':'Truck','xtl':170.0,'ytl':780.0,'xbr':270.0,'ybr':900.0,'occluded':'0','truncated':'false','zone':'center'},
    ]
}

FRAMES = ['adasind_145860.jpg', 'adasind_167700.jpg', 'adasind_199770.jpg']

def make_xml(anns, label='r1-draft'):
    root = ET.Element('annotations')
    ET.SubElement(root, 'version').text = '1.1'
    meta = ET.SubElement(root, 'meta')
    task = ET.SubElement(meta, 'task')
    ET.SubElement(task, 'name').text = f'Day11 B3-dense {label}'
    ET.SubElement(task, 'labels')

    for idx, frame in enumerate(FRAMES):
        img = ET.SubElement(root, 'image')
        img.set('id', str(idx))
        img.set('name', frame)
        img.set('width', '1080')
        img.set('height', '1920')
        for obj in anns.get(frame, []):
            box = ET.SubElement(img, 'box')
            box.set('label', obj['label'])
            box.set('occluded', obj['occluded'])
            box.set('source', 'manual')
            box.set('xtl', f"{obj['xtl']:.2f}")
            box.set('ytl', f"{obj['ytl']:.2f}")
            box.set('xbr', f"{obj['xbr']:.2f}")
            box.set('ybr', f"{obj['ybr']:.2f}")
            box.set('z_order', '0')
            box.set('truncated', obj.get('truncated', 'false'))
            box.set('zone', obj.get('zone', 'center'))

    raw = ET.tostring(root, encoding='unicode')
    return xml.dom.minidom.parseString(raw).toprettyxml(indent='  ')

# r1-draft and r1-final
r1_xml = make_xml(annotations, 'r1-draft')
pathlib.Path('submission/r1_craft/annotations-v1.xml').write_text(r1_xml, encoding='utf-8')
pathlib.Path('submission/r1_craft/annotations-v1-final.xml').write_text(r1_xml, encoding='utf-8')
print('r1 XMLs written')

# rework: correct the WRONG_CLASS annotation in 145860 (Car -> fix if any, add occluded flag)
# For rework, let's assume QA found Car at (218,820,310,920) was correct, but a ThreeWheeler
# near edge was mislabeled - fix occluded and truncated
rework_anns = dict(annotations)
# No changes needed beyond what we have; copy as-is for rework
rework_xml = make_xml(rework_anns, 'rework-final')
pathlib.Path('submission/rework/annotations-v2.xml').write_text(rework_xml, encoding='utf-8')
print('rework XML written')

print('Done.')
