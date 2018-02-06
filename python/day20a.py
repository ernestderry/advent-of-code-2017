class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def changeVelocity(self):
        for axis in range(3):
            self.velocity[axis] += self.acceleration[axis]

    def changePosition(self):
        for axis in range(3):
            self.position[axis] += self.velocity[axis]

    def getPosition(self):
        return self.position

    def calculateDistance(self):
        return reduce(lambda a, b :abs(a) + abs(b), self.position)

    def getMovingAwayFrom000(self):
        return self.movingAwayFrom000

def extractValues(text, valueSet):
    parts = text.split(", ")
    bracketIndex = parts[valueSet].index(">")
    values = map(int, parts[valueSet][3:bracketIndex].split(','))
    return values

p = Particle([3,3,3], [2,2,2], [-1,-1,-1])
p.changeVelocity()
p.changePosition()
print p.getPosition()[0] == 4
print p.getPosition()[1] == 4
print p.getPosition()[2] == 4

p.changeVelocity()
p.changePosition()
print p.getPosition()[0] == 4
print p.getPosition()[1] == 4
print p.getPosition()[2] == 4

p.changeVelocity()
p.changePosition()
print p.getPosition()[0] == 3
print p.getPosition()[1] == 3
print p.getPosition()[2] == 3

print p.calculateDistance() == 9

p = Particle([4,4,4], [0,0,0], [-2,-2,-2])
p.changeVelocity()
p.changePosition()
print p.getPosition()[0] == 2
print p.getPosition()[1] == 2
print p.getPosition()[2] == 2

p.changeVelocity()
p.changePosition()

print p.getPosition()[0] == -2
print p.getPosition()[1] == -2
print p.getPosition()[2] == -2

p.changeVelocity()
p.changePosition()
print p.getPosition()[0] == -8
print p.getPosition()[1] == -8
print p.getPosition()[2] == -8

print p.calculateDistance() == 24

particles = []
f = open("c:\\temp\\adcode.txt", 'r')
for line in f:
    position = extractValues(line, 0)
    velocity = extractValues(line, 1)
    acceleration = extractValues(line, 2)

    particle = Particle(position, velocity, acceleration)
    particles.append(particle)

while True:
    for p in particles:
        p.changeVelocity()
        p.changePosition()

    shortestDistance = particles[0].calculateDistance()
    shortestParticle = 0
    for p_idx in range(1, len(particles)):
        if particles[p_idx].calculateDistance() < shortestDistance:
            shortestDistance = particles[p_idx].calculateDistance()
            shortestParticle = p_idx

    print shortestParticle, shortestDistance
