with open("associations.txt") as f:
	content = f.readlines()
content = [x.strip() for x in content]

airplane = []
basket = []
plastic = []
spirit = []
festival = []
pink = []
earth = []
quarter = []
meltdown = []
lucky = []

for line in content:
	if "airplane" in line and "basket" in line and "plastic" in line and "spirit" in line and "festival" in line and "pink" in line and "earth" in line and "quarter" in line and "meltdown" in line:
		lucky.append(line)
	if "airplane" in line:
		airplane.append(line)
	if "basket" in line:
		basket.append(line)
	if "plastic" in line:
		plastic.append(line)
	if "spirit" in line:
		spirit.append(line)
	if "festival" in line:
		festival.append(line)
	if "pink" in line:
		pink.append(line)
	if "earth" in line:
		earth.append(line)
	if "quarter" in line:
		quarter.append(line)
	if "meltdown" in line:
		meltdown.append(line)

for line in airplane:
	
