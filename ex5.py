name = 'Zed A.Shaw'
age = 35 
height = 74
weight = 180
eyes= 'Blue'
teeth = 'White'
hair = 'Brown'
convert = height * 2.54
convertWeight = weight *2.20462
print "Let's talk about %s." % name
print "He's %d centimeters tall." % convert
print "He's %d kilograms heavy." % convertWeight
print "Actually  that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d, and %d, I get %d." %(age, convert, convertWeight, age + convert + convertWeight)