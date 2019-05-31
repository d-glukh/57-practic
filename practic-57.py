from copy import deepcopy
import random
def choose0(rows, deck0, deck1):
	card = deck1[random.randint(0, len(deck1)-1)]
	return card

def choose(rows, deck0, deck1):
	index = 0
	minexpval = 1000000000
	for i in range(len(deck1)):
		expval = 0
		for j in range(len(deck0)):
			rows1 = deepcopy(rows)
			deck01 = deepcopy(deck0)
			deck11 = deepcopy(deck1)
			extraptss = move_im(deck0[j], deck1[i], rows1)
			deck01.pop(j)
			deck11.pop(i)
			expval += ocenka1(rows1, deck01, deck11, extraptss, 2)
		if expval < minexpval:
			minexpval = expval
			index = i
	card = deck1[index]
	return card

def ocenka1(o_rows, o_deck0, o_deck1, o_ptsadd, depth):
	if depth == 0:
		return o_ptsadd[1] - o_ptsadd[0]
	else:
		o_minexpval = 1000000000
		for k in range(len(o_deck1)):
			o_expval = 0
			for l in range(len(o_deck0)):
				o_rows1 = deepcopy(o_rows)
				o_deck01 = deepcopy(o_deck0)
				o_deck11 = deepcopy(o_deck1)
				o_extrapts = move_im(o_deck0[l], o_deck1[k], o_rows1)
				o_deck01.pop(l)
				o_deck11.pop(k)
				o_expval += ocenka1(o_rows1, o_deck01, o_deck11, [o_extrapts[0] + o_ptsadd[0], o_extrapts[1] + o_ptsadd[1]], depth-1)
			if o_expval < o_minexpval:
				o_minexpval = o_expval
	return o_minexpval

def move_im(c0, c1, rows):
	p0add = 0
	p1add = 0
	if c0 < c1: #у игрока меньше карта
		if c0 < min([i[-1] for i in rows]): #меньше чем все карты в рядах
			minpts = 1000
			for i in range(4):
				if points(rows[i]) < minpts:
					minpts = points(rows[i])
					e = i
			p0add += points(rows[e])
			rows[e] = [c0]
		else: #есть куда положить
			diff = [25, 25, 25, 25]
			for i in range(4):
				if rows[i][-1] < c0:
					diff[i] = c0 - rows[i][-1]
			e = diff.index(min(diff))
			if len(rows[e]) == 5:
				p0add += points(rows[e])
				rows[e] = [c0]
			else:
				rows[e].append(c0)
		diff = [25, 25, 25, 25] #куда пойдет карта компа
		for i in range(4):
				if rows[i][-1] < c1:
					diff[i] = c1 - rows[i][-1]
		e = diff.index(min(diff))
		if len(rows[e]) == 5:
			p1add += points(rows[e])
			rows[e] = [c1]
		else:
			rows[e].append(c1)
	else: #тоже самое если у компа меньше карта
		if c1 < min([i[-1] for i in rows]):
			# e = random.randint(0, 3)
			minpts = 1000
			for i in range(4):
				if points(rows[i]) < minpts:
					minpts = points(rows[i])
					e = i
			p1add += points(rows[e])
			rows[e] = [c1]
		else:
			diff = [25, 25, 25, 25]
			for i in range(4):
				if rows[i][-1] < c1:
					diff[i] = c1 - rows[i][-1]
			e = diff.index(min(diff))
			if len(rows[e]) == 5:
				p1add += points(rows[e])
				rows[e] = [c1]
			else:
				rows[e].append(c1)
		diff = [25, 25, 25, 25]
		for i in range(4):
				if rows[i][-1] < c0:
					diff[i] = c0 - rows[i][-1]
		e = diff.index(min(diff))
		if len(rows[e]) == 5:
			p0add += points(rows[e])
			rows[e] = [c0]
		else:
				rows[e].append(c0)
	return [p0add, p1add]

def move(c0, c1, rows):
	p0add = 0
	p1add = 0
	if c0 < c1: #у игрока меньше карта
		if c0 < min([i[-1] for i in rows]): #меньше чем все карты в рядах
			print('Choose one row to take:              <enter one integer from 1 to 4>')
			e = input()
			while not (e == '1' or e == '2' or e == '3' or e == '4'):
				if e.isdigit():
					print('There is no such row, must be integer 1 to 4, try again')
				else:
					print('Wrong input format, must be integer 1 to 4, try again')
				e = input()
			p0add += points(rows[int(e)-1])
			rows[int(e)-1] = [c0]
		else: #есть куда положить
			diff = [25, 25, 25, 25]
			for i in range(4):
				if rows[i][-1] < c0:
					diff[i] = c0 - rows[i][-1]
			e = diff.index(min(diff))
			if len(rows[e]) == 5:
				p0add += points(rows[e])
				rows[e] = [c0]
			else:
				rows[e].append(c0)
		diff = [25, 25, 25, 25] #куда пойдет карта компа
		for i in range(4):
				if rows[i][-1] < c1:
					diff[i] = c1 - rows[i][-1]
		e = diff.index(min(diff))
		if len(rows[e]) == 5:
			p1add += points(rows[e])
			rows[e] = [c1]
		else:
			rows[e].append(c1)
	else: #тоже самое если у компа меньше карта
		if c1 < min([i[-1] for i in rows]):
			# e = random.randint(0, 3)
			minpts = 1000
			for i in range(0, 4):
				if points(rows[i]) < minpts:
					minpts = points(rows[i])
					e = i
			p1add += points(rows[e])
			rows[e] = [c1]
		else:
			diff = [25, 25, 25, 25]
			for i in range(4):
				if rows[i][-1] < c1:
					diff[i] = c1 - rows[i][-1]
			e = diff.index(min(diff))
			if len(rows[e]) == 5:
				p1add += points(rows[e])
				rows[e] = [c1]
			else:
				rows[e].append(c1)
		diff = [25, 25, 25, 25]
		for i in range(4):
				if rows[i][-1] < c0:
					diff[i] = c0 - rows[i][-1]
		e = diff.index(min(diff))
		if len(rows[e]) == 5:
			p0add += points(rows[e])
			rows[e] = [c0]
		else:
				rows[e].append(c0)
	return [p0add, p1add]

def points(r):
	pts = 0
	for i in r:
		if i == 55:
			pts += 7
		elif i%10 == 0:
			pts += 3
		elif i%5 == 0:
			pts += 2
		elif i%11 == 0:
			pts += 5
		else:
			pts += 1
	return(pts)

deck = range(1, 25)
deck0 = random.sample(deck, 10)
deck = list(set(deck) - set(deck0))
deck1 = random.sample(deck, 10)
deck  = list(set(deck) - set(deck1))
rowsreal = [[deck[0]], [deck[1]], [deck[2]], [deck[3]]]
p = [0, 0]
c = [0, 0]
print('Hello! You are about to play the "Cow 006" game.\nFor rules and instructions check attached text file.\nGood luck and have fun!\n\n\n')
print('Rows:')
for i in deck:
	print(i)
for f in range(10):
	print('Choose one of your cards for the move. Your deck:', deck0)
	inp = input()
	while (not inp.isdigit()) or (int(inp) not in deck0):
		if not inp.isdigit():
			print('Wrong input format, must be number, try again')
		else:
			print('There is no such card in your deck, try again')
		inp = input()
	c[0] = deck0.pop(deck0.index(int(inp)))
	c[1] = choose(list(rowsreal), deck0, deck1)
	deck1.pop(deck1.index(c[1]))
	print('Opponent move:', c[1])
	add = move(c[0], c[1], rowsreal)
	p[0] += add[0]
	p[1] += add[1]
	print('Rows:')
	for i in rowsreal:
		print(*i)
	print('Your points:', p[0])
	print('Opponent points:', p[1])
if p[0] > p[1]:
	print('Computer won, better luck next time!')
if p[0] == p[1]:
	print('Draw')
if p[0] < p[1]:
	print('Congratulations, you won!')
k = input('To finish the program print something:')