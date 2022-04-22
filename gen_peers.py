f = open('large.xml', 'w')

tab = 0
def fpr(s):
  f.write(' ' * tab)
  f.write(s)
  f.write('\n')

fpr('<?xml version=\'1.0\'?>')
fpr('<!DOCTYPE platform SYSTEM "https://simgrid.org/simgrid.dtd">')
fpr('<platform version="4.1">')
fpr('  <actor host="node-0.acme.org" function="tracker">')
fpr('    <argument value="3000" />')
fpr('  </actor>')
fpr('')

end_time = 500000
tab = 2

fpr('<actor host="node-1.acme.org" function="peer">')
fpr('  <argument value="00000002"/>    <!-- my id -->')
fpr(f'  <argument value="{end_time}" />    <!-- end time --> ')
fpr('  <argument value="1" />       <!-- indicates if the peer is a seed at the beginning of the simulation --> ')
fpr('</actor>')
fpr('<actor host="node-2.acme.org" function="peer">')
fpr('  <argument value="00000003"/>    <!-- my id -->')
fpr(f'  <argument value="{end_time}" />    <!-- end time --> ')
fpr('  <argument value="1" />       <!-- indicates if the peer is a seed at the beginning of the simulation --> ')
fpr('</actor>')
fpr('')


import sys
cnt = int(sys.argv[1])
print(f"generating {cnt} hosts")

for i in range(cnt):
  fpr(f'<actor host="node-{i+3}.acme.org" function="peer">')
  fpr(f'  <argument value="0000000{i+4}"/>    <!-- my id -->')
  fpr(f'  <argument value="{end_time}" />    <!-- end time --> ')
  fpr('</actor>')
tab = 0
fpr('</platform>')

f.close();
