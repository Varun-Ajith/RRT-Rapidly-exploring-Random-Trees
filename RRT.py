import pygame
from RRTbase import RRTmap
from RRTbase import RRTGraph
import time


def main():
    dimensions = (600, 1200)
    start = (50, 50)
    goal = (510, 510)
    obsDim = 30
    obsNum = 50
    iteration = 0
    t1 = 0

    pygame.init()
    map = RRTmap(start, goal, dimensions, obsDim, obsNum)
    graph = RRTGraph(start, goal, dimensions, obsDim, obsNum)

    obstacles = graph.makeObs()
    map.drawMap(obstacles)

    t1 = time.time()
    while (not graph.path_to_goal()):
        elasped = time.time() - t1
        t1 = time.time()
        if elasped > 10:
            raise
        if iteration % 10 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.Grey, (X[-1], Y[-1]), map.nodeRad + 2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)
        else:
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.Grey, (X[-1], Y[-1]), map.nodeRad + 2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)
        if iteration % 5 == 0:
            pygame.display.update()
        iteration += 1
    map.drawPath(graph.getpathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)


if __name__ == '__main__':
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False
