class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        arrow = 1
        arrows = points[0][1]
        for start, end in points [1:]:
            if start > arrows:
                arrow += 1
                arrows = end
        return arrow