class Solution:
    def averageWaitingTime(self, customers):
        chef_availability = 0
        total_wait = 0

        for customer_arrival, recipe_duration in customers:
            start_time = max(chef_availability, customer_arrival)
            customer_wait = recipe_duration

            if customer_arrival < chef_availability:
                customer_wait += chef_availability - customer_arrival

            chef_availability = start_time + recipe_duration
            total_wait += customer_wait

        return total_wait / len(customers)