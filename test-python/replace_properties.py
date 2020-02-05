import sys, shutil
print(sys.path);
tf= 'infrastructure_configuration.txt'
src_config_file='pelicansos.xml'
dst_config_file='pelicansos2.xml'
f = open(tf,'r')
f_src = open(src_config_file,'r')
f_dst = open(dst_config_file,'w')
readed_lines = f.readlines()
f_src_readed_lines = f_src.readlines()
for line_src in f_src_readed_lines:
    for line in readed_lines:
        line_items = line.strip().split('=')
        line_src = line_src.replace('${'+line_items[0]+'}',line_items[1])
    f_dst.write(line_src)
f_src.close()
f.close()
f_dst.close()
shutil.move(dst_config_file,src_config_file)
