import unittest


class TestAggregatedThreatScore(unittest.TestCase):
    def test_calculate_aggregated_threat_score_equal_importance(self):
        department_scores = [
            generate_random_data(30, 5, 50),
            generate_random_data(32, 5, 50),
            generate_random_data(28, 5, 50),
            generate_random_data(31, 5, 50),
            generate_random_data(29, 5, 50)
        ]
        importance_tags = [3, 3, 3, 3, 3]
        result = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_calculate_aggregated_threat_score_different_importance(self):
        # Test case 2: Different importance levels
        department_scores = [
            generate_random_data(30, 10, 100),
            generate_random_data(60, 10, 100),
            generate_random_data(20, 10, 100),
            generate_random_data(40, 10, 100),
            generate_random_data(10, 10, 100)
        ]
        importance_tags = [1, 5, 2, 3, 4]
        result = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_calculate_aggregated_threat_score_different_sizes(self):
        # Test case 3: Different department sizes
        department_scores = [
            generate_random_data(30, 10, 150),
            generate_random_data(60, 10, 75),
            generate_random_data(20, 10, 200),
            generate_random_data(40, 10, 50),
            generate_random_data(10, 10, 120)
        ]
        importance_tags = [3, 3, 3, 3, 3]
        result = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_calculate_aggregated_threat_score_with_outliers(self):
        # Test case 4: Presence of outliers
        department_scores = [
            generate_random_data(10, 5, 100),
            generate_random_data(50, 5, 100),
            generate_random_data(30, 5, 100),
            [90] * 5 + generate_random_data(30, 5, 95),  # Department with outliers
            generate_random_data(40, 5, 100)
        ]
        importance_tags = [2, 2, 2, 2, 2]
        result = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

    def test_calculate_aggregated_threat_score_no_importance(self):
        # Test case 5: No importance tags (all 0s)
        department_scores = [
            generate_random_data(10, 5, 50),
            generate_random_data(20, 5, 50),
            generate_random_data(30, 5, 50),
            generate_random_data(40, 5, 50),
            generate_random_data(50, 5, 50)
        ]
        importance_tags = [0, 0, 0, 0, 0]
        result = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertEqual(result, 0)

    def test_calculate_aggregated_threat_score_edge_values(self):
        # Test case 6: Edge values (0s and 90s)
        department_scores = [
            [0] * 100,
            [90] * 100,
            generate_random_data(45, 0, 100),  # 45 across 100 users
            generate_random_data(90, 0, 100),  # All maxed out at 90
            generate_random_data(0, 0, 100)  # All set to 0
        ]
        importance_tags = [1, 1, 1, 1, 1]
        result = calculate_aggregated_threat_score(department_scores, importance_tags)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, 90)

if __name__ == '__main__':
    unittest.main()
