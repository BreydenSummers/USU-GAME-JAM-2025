class Lerp:
    def __init__(self, start, end, range_start, range_end):
        self.start = start
        self.end = end
        
        self.range_start = range_start
        self.range_end = range_end

    def interpolate(self, progress):
        progress = (progress - self.range_start) / (self.range_end - self.range_start)
        x = ((self.end[0] - self.start[0]) * progress) + self.start[0]
        y = ((self.end[1] - self.start[1]) * progress) + self.start[1]

        return [x, y]
    
    def test_range(self, progress):
        if progress > self.range_end:
            return False
        if progress < self.range_start:
            return False
        return True