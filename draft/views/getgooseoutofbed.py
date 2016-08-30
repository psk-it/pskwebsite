import random
def  makegoosegetoutofbed(inbed = True):
	while inbed:
		n_alarms = random.randrange(1, 8)
		s = "GET THE FUCK OUT OF BED"
		print (s + "\n") * (n_alarms - 1) + sBa
		inp = raw_input("Is Michael in bed? : ")
		inbed = inp.lower() in ['yes', 'y', 't', 'true']
	number_of_kisses = random.randrange(5, 25)
	print "Come get %i kisses gooseman" % number_of_kisses
	return number_of_kisses
makegoosegetoutofbed()