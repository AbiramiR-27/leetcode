class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)

        ones_img1 = []
        ones_img2 = []
        
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    ones_img1.append((r, c))
                if img2[r][c] == 1:
                    ones_img2.append((r, c))
        translation_counts = {}
        max_overlap = 0
        for r1, c1 in ones_img1:
            for r2, c2 in ones_img2:
                vec = (r2 - r1, c2 - c1)
                translation_counts[vec] = translation_counts.get(vec, 0) + 1
             
                if translation_counts[vec] > max_overlap:
                    max_overlap = translation_counts[vec]
                    
        return max_overlap  