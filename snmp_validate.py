from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get, napalm_validate

nr = InitNornir(config_file="config.yaml")

get_snmp = nr.run(name="GATHERING SNMP", task=napalm_get, getters=["get_snmp_information"])

print_result(get_snmp)

validate = nr.run(name="VALIDATE SNMP", task=napalm_validate, src="./validate/cisco.yaml")

print_result(validate)
