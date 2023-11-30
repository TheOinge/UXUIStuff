import pandas as pd
import matplotlib.pyplot as plt

def generate_graphs():
    # Read data from CSV file
    df = pd.read_csv('data.csv')

    # Plotting
    plot_failed_pages(df)
    plot_easiness(df)
    plot_time(df)
    plot_clicks(df)
    plot_errors(df)

    # Show all plots
    plt.show()

def plot_failed_pages(df):
    plt.figure(figsize=(8, 6))
    df['Name'].value_counts().plot(kind='bar', color=['red', 'green'])
    plt.title('Failed Pages Distribution')
    plt.xlabel('Name')
    plt.ylabel('Count')
    plt.show()

def plot_easiness(df):
    plt.figure(figsize=(8, 6))
    df.plot(x='Name', y='Easiness', kind='bar', color='skyblue')
    plt.title('Easiness Distribution')
    plt.xlabel('Name')
    plt.ylabel('Easiness Rating')
    plt.show()

def plot_time(df):
    plt.figure(figsize=(8, 6))
    df.plot(x='Name', y='Time', kind='bar', color='orange')
    plt.title('Time Distribution')
    plt.xlabel('Name')
    plt.ylabel('Time (seconds)')
    plt.show()

def plot_clicks(df):
    plt.figure(figsize=(8, 6))
    df.plot(x='Name', y='Clicks', kind='bar', color='purple')
    plt.title('Clicks Distribution')
    plt.xlabel('Name')
    plt.ylabel('Number of Clicks')
    plt.show()

def plot_errors(df):
    plt.figure(figsize=(8, 6))
    df.plot(x='Name', y='Errors', kind='bar', color='red')
    plt.title('Errors Distribution')
    plt.xlabel('Name')
    plt.ylabel('Number of Errors')
    plt.show()

if __name__ == "__main__":
    generate_graphs()
