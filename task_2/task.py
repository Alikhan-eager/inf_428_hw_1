import numpy as np

def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_threat_score(department_scores, importance_tags):
	total_score = 0
	total_importance = 0

	for i, scores in enumerate(department_scores):
		department_mean_score = np.mean(scores)
		importance = importance_tags[i]
		total_score += department_mean_score * importance
		total_importance += importance

	if total_importance == 0:
		return 0

	return min(90, max(0, total_score / total_importance))
