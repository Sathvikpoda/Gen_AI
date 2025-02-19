import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_and_process_data(file_path):
    """Loads and processes the smartphone dataset."""
    df = pd.read_csv(file_path)
    if 'Price' in df.columns:
        df['Price'] = pd.to_numeric(df['Price'].replace('[\$,]', '', regex=True), errors='coerce')
    if 'Rating' in df.columns:
        df['Rating'] = pd.to_numeric(df['Rating'].replace('No Rating', pd.NA), errors='coerce')
    if 'Reviews' in df.columns:
        df['Reviews'] = pd.to_numeric(df['Reviews'].replace('No Reviews', pd.NA), errors='coerce')
    return df

def get_top_5_smartphones(df):
    """Returns the top 5 smartphones under ₹50,000 based on price."""
    return df[df['Price'] < 50000].sort_values('Price', ascending=False).head(5)

def print_top_5_smartphones(top_5_smartphones):
    """Prints the details of the top 5 smartphones."""
    print("Top 5 Smartphones under ₹50,000:")
    for index, row in top_5_smartphones.iterrows():
        print(f"{index + 1}. {row['Title']}")
        print(f"   Price: ₹{row['Price']:,.2f}")
        print(f"   Rating: {row['Rating'] if pd.notna(row['Rating']) else 'No Rating'}")
        print(f"   Reviews: {row['Reviews'] if pd.notna(row['Reviews']) else 'No Reviews'}")
        print("-" * 50)

def find_best_phone_in_category(top_5_smartphones, category):
    """Finds the best phone based on the specified category."""
    if category == 'Price':
        best_phone = top_5_smartphones.loc[top_5_smartphones[category].idxmin()]
    else:
        best_phone = top_5_smartphones.loc[top_5_smartphones[category].idxmax()]
    return best_phone['Title'], best_phone[category]

def display_phone_bar_chart(top_5_smartphones, spec):
    """Displays a bar chart to compare the top 5 smartphones based on the specified specification."""
    if spec not in top_5_smartphones.columns:
        print(f"Specification '{spec}' not found in the dataset.")
        return

    # Sort phones based on the specification
    if spec.lower() == 'price':
        sorted_phones = top_5_smartphones.sort_values(spec, ascending=True)
    else:
        sorted_phones = top_5_smartphones.sort_values(spec, ascending=False)

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the bar chart
    bars = ax.bar(sorted_phones['Title'], sorted_phones[spec], color='blue')

    # Highlight the best phone
    bars[0].set_color('red')

    # Add value labels on the top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height, 
                f'{height:.2f}' if spec.lower() != 'reviews' else f'{height:.0f}', 
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Customize the plot
    plt.title(f"Phone Comparison by {spec}")
    plt.xlabel("Smartphones")
    plt.ylabel(spec)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Show the plot
    plt.show()

    # Print all values and suggest the best phone
    print(f"\n{spec} for all phones in the top 5:")
    for index, row in sorted_phones.iterrows():
        print(f"{row['Title']}: {row[spec]}")
    
    best_phone = sorted_phones.iloc[0]
    if spec.lower() == 'price':
        print(f"\nBased on {spec}, the best phone among the top 5 is: {best_phone['Title']}")
        print(f"It has the lowest price of ₹{best_phone[spec]:,.2f}")
    elif spec.lower() == 'rating':
        print(f"\nBased on {spec}, the best phone among the top 5 is: {best_phone['Title']}")
        print(f"It has the highest rating of {best_phone[spec]}")
    elif spec.lower() == 'reviews':
        print(f"\nBased on {spec}, the best phone among the top 5 is: {best_phone['Title']}")
        print(f"It has the highest number of reviews: {best_phone[spec]:,.0f}")

def display_overall_best_phone_bar_chart(top_5_smartphones):
    """Displays the overall best phone by combining scores from all categories using a bar chart."""
    categories = ['Price', 'Rating', 'Reviews']
    scores = {title: 0 for title in top_5_smartphones['Title']}

    for category in categories:
        if category not in top_5_smartphones.columns:
            continue
        sorted_phones = top_5_smartphones.sort_values(category, ascending=(category == 'Price'))
        for rank, title in enumerate(sorted_phones['Title']):
            scores[title] += (len(sorted_phones) - rank)

    # Find the overall best phone based on the highest score
    best_phone = max(scores, key=scores.get)
    best_score = scores[best_phone]

    # Plot the bar chart for the overall scores
    plt.figure(figsize=(12, 8))
    bars = plt.bar(scores.keys(), scores.values(), color='blue')

    # Highlight the best phone
    best_index = list(scores.keys()).index(best_phone)
    bars[best_index].set_color('red')

    plt.title("Overall Best Smartphone Based on All Categories")
    plt.xlabel("Smartphones")
    plt.ylabel("Combined Score")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

# Main execution
file_path = r"C:\Users\sathv\Downloads\dataset.csv"
df = load_and_process_data(file_path)
top_5_smartphones = get_top_5_smartphones(df)

print_top_5_smartphones(top_5_smartphones)

# Print available columns for comparison
print("\nAvailable specifications:")
specs = [col for col in top_5_smartphones.columns if col.lower() not in ['title', 'image url', 'product url']]
for i, spec in enumerate(specs):
    print(f"{i+1}. {spec}")

while True:
    user_input = input("\nEnter the specification you want to compare (Rating, Reviews, Price), or 'exit' to quit: ")
    
    if user_input.lower() == 'exit':
        print("Thank you for using our smartphone recommender. Goodbye!")
        break
    
    if user_input.lower() in ['rating', 'reviews', 'price']:
        spec = user_input.capitalize()
        display_phone_bar_chart(top_5_smartphones, spec)
        
        # Find the best phone among all smartphones for the chosen specification
        best_phone, best_value = find_best_phone_in_category(df, spec)
        print(f"\nThe best phone among all smartphones for {spec} is: {best_phone} with a {spec.lower()} of {best_value}")
    else:
        print("Invalid specification. Please choose from Rating, Reviews, or Price.")
