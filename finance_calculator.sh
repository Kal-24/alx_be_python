#!/bin/bash

read -p "Enter your monthly income: " monthly_income
read -p "Enter your total monthly expenses: " monthly_expenses

monthly_savings=$(echo "$monthly_income - $monthly_expenses" | bc)

interest_rate=0.05

projected_savings=$(echo "scale=2; $monthly_savings * 12 * (1 + $interest_rate)" | bc)

printf "Your monthly savings are \$%.2f.\n" "$monthly_savings"
printf "Projected savings after one year, with interest, is: \$%.2f.\n" "$projected_savings"
