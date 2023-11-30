import pandas as pd
import matplotlib.pyplot as plt

def calculate_statistics(df):
    # Calculate mean and standard deviation for the entire dataset
    overall_mean = df[['Time', 'Clicks', 'Errors']].mean()
    overall_std = df[['Time', 'Clicks', 'Errors']].std()
    easiness_mean = df['Easiness'].mean()
    easiness_std = df['Easiness'].std()

    return overall_mean, overall_std, easiness_mean, easiness_std

def plot_statistics(overall_mean, overall_std, easiness_mean, easiness_std):
    # Display the calculated statistics
    print("Overall Data Statistics:")
    print("Mean (excluding Easiness):")
    print(overall_mean)
    print("\nStandard Deviation (excluding Easiness):")
    print(overall_std)
    print("\nEasiness Mean:")
    print(easiness_mean)
    print("\nEasiness Standard Deviation:")
    print(easiness_std)

    # Plotting overall means with error bars (standard deviations)
    plt.figure(figsize=(12, 6))

    # Plot for Easiness
    plt.subplot(1, 2, 1)
    plt.bar(['Easiness'], [easiness_mean], yerr=easiness_std, color='skyblue', capsize=5)
    plt.title('Easiness Mean with Standard Deviation')
    plt.ylabel('Mean Value')

    # Plot for other categories
    plt.subplot(1, 2, 2)
    plt.bar(overall_mean.index, overall_mean, yerr=overall_std, color=['orange', 'purple', 'red'], capsize=5)
    plt.title('Overall Mean (excluding Easiness) with Standard Deviation')
    plt.ylabel('Mean Value')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Read data from CSV file
    df = pd.read_csv('data.csv')

    # Calculate statistics
    overall_mean, overall_std, easiness_mean, easiness_std = calculate_statistics(df)

    # Plot and display statistics
    plot_statistics(overall_mean, overall_std, easiness_mean, easiness_std)
