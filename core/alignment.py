from difflib import SequenceMatcher
import numpy as np

class SequenceAligner:
    @staticmethod
    def smith_waterman(seq1: str, seq2: str, match=2, mismatch=-1, gap=-1):
        """Local alignment with affine gap penalties"""
        m, n = len(seq1), len(seq2)
        score_matrix = np.zeros((m+1, n+1))
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                match_score = score_matrix[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
                delete = score_matrix[i-1][j] + gap
                insert = score_matrix[i][j-1] + gap
                score_matrix[i][j] = max(0, match_score, delete, insert)
        
        return np.max(score_matrix)
