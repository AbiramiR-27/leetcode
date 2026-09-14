class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        overlap_x = rec1[0] < rec2[2] and rec2[0] < rec1[2]
        overlap_y = rec1[1] < rec2[3] and rec2[1] < rec1[3]
        
        return overlap_x and overlap_y