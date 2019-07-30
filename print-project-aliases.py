#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python
#HEN
# alias vimhen='vim /opt/odoo/12.0-HEN'
# alias ihen='sudo /opt/odoo/12.0-HEN/dev_tools/odoo-scripts/odoo-server'
# alias hen='cd /opt/odoo/12.0-HEN/12.0'
# alias hen-log='tail -f /opt/odoo/12.0-HEN/logs/odoo-server.log'
# alias eohen='eo -data /home/harmony/workspace/HEN -showlocation &'

import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("name", help="customer name in short")
parser.add_argument("version", help="customer instance version")
args = parser.parse_args()

ODOO_BASE = os.path.abspath('/opt/odoo')
CONF_BASE = os.path.abspath('/opt/odoo/alias_conf')
eclispse_workspace_base = os.path.abspath('/home/harmony/workspace')

name=args.name
ver=args.version
ver_name = '{0}-{1}'.format(ver, name.upper())
customer_path  = os.path.join(ODOO_BASE, '{ver_name}/src'.format(ver_name=ver_name))
init_script_path = os.path.join(customer_path, 'dev_tools/odoo-scripts/odoo-server')
odoo_exec_path  = os.path.join(customer_path, '{0}'.format(ver))
log_path  = os.path.join(customer_path, 'logs/odoo-server.log')
customer_work_space = os.path.join(eclispse_workspace_base, ver_name)
if not os.path.isdir(customer_work_space):
    os.makedirs(customer_work_space)

var_dict = {
        'name':name,
        'name_caps': name.upper(),
        'odoo_base': ODOO_BASE,
        'ver_name':ver_name,
        'customer_path': customer_path,
        'odoo_exec_path': odoo_exec_path,
        'init_script_path':init_script_path,
        'log_path':log_path,
        'customer_work_space':customer_work_space,
        'ver':ver,
        }


alias = """
#{name_caps}
alias vim{name}-{ver}='vim {customer_path}'
alias i{name}-{ver}='sudo {init_script_path}'
alias {name}-{ver}='cd {odoo_exec_path}'
alias {name}-{ver}-log='tail -f {log_path}'
alias eo{name}-{ver}='eo -data {customer_work_space} -showlocation &'
""".format(**var_dict)

customer_alias_filename = '{name}_{ver}_alias.sh'.format(name=name,ver=ver)
customer_conf_path = os.path.join(CONF_BASE, customer_alias_filename)

with open(customer_conf_path, 'w') as f:
    f.write(alias)

print customer_conf_path

