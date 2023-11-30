import pandas as pd
import matplotlib.pyplot as plt

def calculate_statistics(df):
    # Calculate mean and standard deviation for the entire dataset
    overall_mean = df[['Easiness', 'Time', 'Clicks', 'Errors']].mean()
    overall_std = df[['Easiness', 'Time', 'Clicks', 'Errors']].std()

    return overall_mean, overall_std

def plot_statistics(overall_mean, overall_std):
    # Display the calculated statistics
    print("Overall Data Statistics:")
    print("Mean:")
    print(overall_mean)
    print("\nStandard Deviation:")
    print(overall_std)

    # Plotting overall means with error bars (standard deviations)
    plt.figure(figsize=(12, 6))

    plt.bar(overall_mean.index, overall_mean, yerr=overall_std, color=['skyblue', 'orange', 'purple', 'red'], capsize=5)
    plt.title('Overall Mean with Standard Deviation')
    plt.xlabel('Category')
    plt.ylabel('Mean Value')

    plt.show()

if __name__ == "__main__":
    # Read data from CSV file
    df = pd.read_csv('data.csv')

    # Calculate overall statistics
    overall_mean, overall_std = calculate_statistics(df)

    # Plot and display overall statistics
    plot_statistics(overall_mean, overall_std)
