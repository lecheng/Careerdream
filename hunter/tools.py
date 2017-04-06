import os
from careerdream.settings import MEDIA_ROOT
from hunter.rater import processResume


def grade_resume(r):
	root = MEDIA_ROOT
	filepath = os.path.join(root, str(r.resume))
	score = processResume(filepath)
	r.score = score
	r.save()
