import random

#def generate_random_ip():
	#return f"192.168.1.{random.randint(0,20)}"

def check_fireRules(ip_Add,fireRules):
	for rule_ip, action in fireRules.items():
		if ip_Add==rule_ip:
			return action
	return "BLOCK"

def main():
	fireRules={
		"192.168.1.1":"ALLOW", #list of allowed ip addresses
		"192.168.1.4":"ALLOW",
		"192.168.1.6":"ALLOW",
		"192.168.1.13":"ALLOW",
		"192.168.1.16":"ALLOW",
		"192.168.1.9":"ALLOW"
		}
	for _ in range(12):  #generates 12 ip address
		ip_Add=input("ENTER IP:")
		action=check_fireRules(ip_Add,fireRules)
		randNum=random.randint(0,9999) #unique id to differentiate
		print(f"IP: {ip_Add}, Action:{action}, Random: {randNum}")
if __name__== "__main__":
	main()

