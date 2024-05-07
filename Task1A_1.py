# generate a sentence 
subject = ['I','You']
verb = ['Play','Love']
object = ['Circket','Ludo ']

# now using these generate a sentence

for s in subject:
	for v in verb:
		for o in object:
			# subject + verb + object
			print(s+' '+v+' '+o) 