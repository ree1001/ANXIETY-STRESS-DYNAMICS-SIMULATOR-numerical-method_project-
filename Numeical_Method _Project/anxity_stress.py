import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Try to import optional packages, install if not available
try:
    from colorama import init, Fore, Back, Style
    COLORAMA_AVAILABLE = True
except ImportError:
    print("Installing colorama...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
    from colorama import init, Fore, Back, Style
    COLORAMA_AVAILABLE = True
    print("colorama installed successfully!")

# Initialize colorama
init(autoreset=True)

# Custom ANSI color codes as fallback
class Colors:
    """ANSI color codes for terminal styling"""
    if COLORAMA_AVAILABLE:
        HEADER = Fore.MAGENTA
        BLUE = Fore.BLUE
        CYAN = Fore.CYAN
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        RED = Fore.RED
        BOLD = Style.BRIGHT
        UNDERLINE = '\033[4m'
        END = Style.RESET_ALL
    else:
        # Fallback ANSI codes
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    # Custom colors
    ANXIETY_LOW = GREEN
    ANXIETY_MED = YELLOW
    ANXIETY_HIGH = '\033[38;5;202m' if COLORAMA_AVAILABLE else YELLOW
    ANXIETY_SEVERE = RED
    
    STRESS_LOW = CYAN
    STRESS_MED = BLUE
    STRESS_HIGH = '\033[38;5;27m' if COLORAMA_AVAILABLE else BLUE
    STRESS_SEVERE = '\033[38;5;90m' if COLORAMA_AVAILABLE else '\033[95m'

# -------------------------------
#  Premium Styling Functions
# -------------------------------

class UI:
    """Premium UI components for terminal interface"""
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_logo():
        """Display premium ASCII logo"""
        logo = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║        █████╗ ███╗   ██╗██╗  ██╗██╗███████╗████████╗██╗   ██╗        ║
║       ██╔══██╗████╗  ██║╚██╗██╔╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝        ║
║       ███████║██╔██╗ ██║ ╚███╔╝ ██║█████╗     ██║    ╚████╔╝         ║
║       ██╔══██║██║╚██╗██║ ██╔██╗ ██║██╔══╝     ██║     ╚██╔╝          ║
║       ██║  ██║██║ ╚████║██╔╝ ██╗██║███████╗   ██║      ██║           ║
║       ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚══════╝   ╚═╝      ╚═╝           ║
║                                                                      ║
║         ███████╗████████╗██████╗ ███████╗███████╗███████╗            ║
║         ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔════╝            ║
║         ███████╗   ██║   ██████╔╝█████╗  ███████╗███████╗            ║
║         ╚════██║   ██║   ██╔══██╗██╔══╝  ╚════██║╚════██║            ║
║         ███████║   ██║   ██║  ██║███████╗███████║███████║            ║
║         ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝            ║
║                                                                      ║
║            🧠 {Colors.YELLOW}ANXIETY & STRESS DYNAMICS SIMULATOR{Colors.CYAN} 🧠                 ║
║             {Colors.GREEN}► Mental Wellness Analytics Platform ◄{Colors.CYAN}                   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{Colors.END}
        """
        print(logo)
    
    @staticmethod
    def print_header(title, subtitle=""):
        """Print a premium styled header"""
        width = 70
        print(f"{Colors.CYAN}{'═' * width}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.CYAN}{'✨' + ' ' * 3}{title.upper():^{width - 10}}{' ' * 3 + '✨'}{Colors.END}")
        if subtitle:
            print(f"{Colors.YELLOW}{subtitle:^{width}}{Colors.END}")
        print(f"{Colors.CYAN}{'═' * width}{Colors.END}")

    @staticmethod
    def print_subheader(title):
        """Print a subheader"""
        print(f"\n{Colors.BLUE}{Colors.BOLD}> {title}{Colors.END}")
        print(f"{Colors.BLUE}{'-' * 70}{Colors.END}")
    
    @staticmethod
    def print_success(msg):
        """Print success message"""
        print(f"{Colors.GREEN}{Colors.BOLD}✅ {msg}{Colors.END}")
    
    @staticmethod
    def print_error(msg):
        """Print error message"""
        print(f"{Colors.RED}{Colors.BOLD}❌ {msg}{Colors.END}")
    
    @staticmethod
    def print_warning(msg):
        """Print warning message"""
        print(f"{Colors.YELLOW}{Colors.BOLD}⚠️  {msg}{Colors.END}")
    
    @staticmethod
    def print_info(msg):
        """Print info message"""
        print(f"{Colors.CYAN}{Colors.BOLD}ℹ️  {msg}{Colors.END}")
    
    @staticmethod
    def print_step(step, total, msg):
        """Print step with progress"""
        print(f"{Colors.YELLOW}[{step}/{total}] {msg}{Colors.END}")
    
    @staticmethod
    def print_loading(text="Loading", duration=1.5):
        """Display loading animation"""
        frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        start_time = time.time()
        i = 0
        while time.time() - start_time < duration:
            print(f"\r{Colors.CYAN}{frames[i % len(frames)]} {text}...{Colors.END}", end="", flush=True)
            i += 1
            time.sleep(0.1)
        print(f"\r{Colors.GREEN}✓ {text} complete!{' ' * 30}{Colors.END}")
    
    @staticmethod
    def animated_bar(value, max_value=10, label="", color=Colors.GREEN):
        """Display animated progress bar"""
        bar_length = 30
        filled_length = int(bar_length * value // max_value)
        bar = f"{color}{'█' * filled_length}{Colors.END}{'░' * (bar_length - filled_length)}"
        percentage = (value / max_value) * 100
        print(f"{label:15} {bar} {percentage:6.1f}%")
    
    @staticmethod
    def person_card(person_id, anxiety, stress, responsiveness=None):
        """Display premium person profile card"""
        avg = (anxiety + stress) / 2
        
        # Determine status and color
        if avg >= 8:
            status = "⚡ SEVERE STRESS"
            status_color = Colors.ANXIETY_SEVERE
            emoji = "🔥"
        elif avg >= 6:
            status = "⚠️  HIGH STRESS"
            status_color = Colors.ANXIETY_HIGH
            emoji = "⚠️"
        elif avg >= 4:
            status = "📊 MODERATE"
            status_color = Colors.ANXIETY_MED
            emoji = "⚡"
        else:
            status = "🌿 MILD"
            status_color = Colors.ANXIETY_LOW
            emoji = "🌱"
        
        # Anxiety color
        if anxiety >= 8:
            anxiety_color = Colors.ANXIETY_SEVERE
        elif anxiety >= 6:
            anxiety_color = Colors.ANXIETY_HIGH
        elif anxiety >= 4:
            anxiety_color = Colors.ANXIETY_MED
        else:
            anxiety_color = Colors.ANXIETY_LOW
        
        # Stress color
        if stress >= 8:
            stress_color = Colors.STRESS_SEVERE
        elif stress >= 6:
            stress_color = Colors.STRESS_HIGH
        elif stress >= 4:
            stress_color = Colors.STRESS_MED
        else:
            stress_color = Colors.STRESS_LOW
        
        print(f"\n{Colors.CYAN}{'╔' + '═' * 56 + '╗'}{Colors.END}")
        print(f"{Colors.CYAN}{'║'}{Colors.END} {Colors.BOLD}{Colors.YELLOW}{'PERSON PROFILE':^54}{Colors.END} {Colors.CYAN}{'║'}{Colors.END}")
        print(f"{Colors.CYAN}{'╠' + '═' * 56 + '╣'}{Colors.END}")
        print(f"{Colors.CYAN}{'║'}{Colors.END} {'ID:':<15} {Colors.BOLD}{Colors.CYAN}{person_id:<40}{Colors.END}{Colors.CYAN}{'║'}{Colors.END}")
        
        if responsiveness:
            print(f"{Colors.CYAN}{'║'}{Colors.END} {'Responsiveness:':<15} ", end="")
            resp_color = Colors.GREEN if responsiveness >= 0.7 else Colors.YELLOW if responsiveness >= 0.4 else Colors.RED
            print(f"{resp_color}{responsiveness:<10.2f}{Colors.END} ", end="")
            bar_length = 30
            filled = int(bar_length * responsiveness)
            bar = f"{resp_color}{'█' * filled}{Colors.END}{'░' * (bar_length - filled)}"
            print(f"{bar}")
        
        print(f"{Colors.CYAN}{'║'}{Colors.END} {'Anxiety:':<15} {anxiety_color}{anxiety:<10.2f}{Colors.END} ", end="")
        bar_length = 30
        filled = int(bar_length * anxiety // 10)
        bar = f"{anxiety_color}{'█' * filled}{Colors.END}{'░' * (bar_length - filled)}"
        print(f"{bar}")
        
        print(f"{Colors.CYAN}{'║'}{Colors.END} {'Stress:':<15} {stress_color}{stress:<10.2f}{Colors.END} ", end="")
        filled = int(bar_length * stress // 10)
        bar = f"{stress_color}{'█' * filled}{Colors.END}{'░' * (bar_length - filled)}"
        print(f"{bar}")
        
        print(f"{Colors.CYAN}{'║'}{Colors.END} {'Average:':<15} {Colors.BOLD}{avg:<10.2f}{Colors.END} ", end="")
        filled = int(bar_length * avg // 10)
        bar = f"{status_color}{'█' * filled}{Colors.END}{'░' * (bar_length - filled)}"
        print(f"{bar}")
        
        print(f"{Colors.CYAN}{'║'}{Colors.END} {'Status:':<15} {status_color}{emoji} {status:<38}{Colors.END}{Colors.CYAN}{'║'}{Colors.END}")
        print(f"{Colors.CYAN}{'╚' + '═' * 56 + '╝'}{Colors.END}")

# -------------------------------
# 🧘‍♂️ Enhanced Relaxation Techniques with Categories
# -------------------------------

relaxations = {
    "Breathing": [
        "Deep Breathing (4-7-8)",
        "Box Breathing",
        "Diaphragmatic Breathing",
        "Alternate Nostril Breathing"
    ],
    "Meditation": [
        "Mindfulness Meditation",
        "Loving-Kindness Meditation",
        "Body Scan Meditation",
        "Transcendental Meditation"
    ],
    "Physical": [
        "Progressive Muscle Relaxation",
        "Yoga (Hatha)",
        "Tai Chi",
        "Gentle Stretching"
    ],
    "Sensory": [
        "Aromatherapy (Lavender)",
        "Music Therapy",
        "Guided Imagery",
        "Nature Sounds"
    ],
    "Creative": [
        "Art Therapy",
        "Journaling",
        "Mandala Coloring",
        "Creative Writing"
    ],
    "Social": [
        "Social Connection",
        "Laughter Therapy",
        "Pet Therapy",
        "Support Group"
    ]
}

# -------------------------------
# 🔢 FIXED Numerical Methods with Realistic Models
# -------------------------------

class WellnessModel:
    """FIXED numerical models for anxiety/stress simulation"""
    
    @staticmethod
    def euler_method(anxiety, stress, technique_type="Physical", dt=1, responsiveness=0.7):
        """FIXED Euler method with realistic psychology"""
        # Different effectiveness based on technique type
        effectiveness = {
            "Breathing": 0.45,
            "Meditation": 0.50,
            "Physical": 0.40,
            "Sensory": 0.35,
            "Creative": 0.30,
            "Social": 0.38
        }
        # Euler method
        # Get effectiveness based on technique and adjust by responsiveness
        k_a = effectiveness.get(technique_type, 0.4) * responsiveness
        k_s = k_a * 0.85  # Stress reduces slightly slower
        
        # REALISTIC MODEL: Anxiety reduces faster when stress is lower
        # Stress reduction benefits from anxiety reduction
        anxiety_reduction = k_a * anxiety * (1 - 0.1 * stress/10)
        stress_reduction = k_s * stress * (1 + 0.05 * anxiety/10)
        
        # Apply reductions
        anxiety_new = anxiety - anxiety_reduction * dt
        stress_new = stress - stress_reduction * dt - 0.08 * anxiety_reduction
        
        # Ensure non-negative values with realistic minimum
        anxiety_new = max(anxiety_new, 0.5)
        stress_new = max(stress_new, 0.5)
        
        return round(anxiety_new, 2), round(stress_new, 2)
    
    @staticmethod
    def rk4_method(anxiety, stress, technique_type="Physical", dt=1, responsiveness=0.7):
        """FIXED RK4 method with proper coupled ODEs"""
        # Different effectiveness based on technique type
        effectiveness = {
            "Breathing": 0.48,
            "Meditation": 0.52,
            "Physical": 0.42,
            "Sensory": 0.37,
            "Creative": 0.32,
            "Social": 0.40
        }
        
        # Get effectiveness based on technique
        base_k = effectiveness.get(technique_type, 0.42)
        k_a = base_k * responsiveness  # Adjusted by personal responsiveness
        k_s = k_a * 0.82  # Stress reduces at different rate
        
        # REALISTIC COUPLED ODEs for anxiety-stress dynamics
        def derivatives(state, t):
            a, s = state
            # Model 1: Anxiety reduces, helped by lower stress
            # Anxiety derivative: reduces based on current anxiety level
            # but slower if stress is high (stress inhibits anxiety reduction)
            da_dt = -k_a * a * (1 - 0.15 * s/10)
            
            # Model 2: Stress reduces, influenced by anxiety
            # Stress derivative: reduces but anxiety makes it harder
            ds_dt = -k_s * s * (1 + 0.08 * a/10)
            
            return np.array([da_dt, ds_dt])
        




        # RK4 implementation for coupled system
        state = np.array([anxiety, stress])
        t = 0  # Current time
        
        k1 = derivatives(state, t)
        k2 = derivatives(state + 0.5 * dt * k1, t + 0.5 * dt)
        k3 = derivatives(state + 0.5 * dt * k2, t + 0.5 * dt)
        k4 = derivatives(state + dt * k3, t + dt)
        
        new_state = state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        
        anxiety_new, stress_new = new_state
        
        # Ensure non-negative values with realistic minimum
        anxiety_new = max(anxiety_new, 0.5)
        stress_new = max(stress_new, 0.5)
        
        return round(anxiety_new, 2), round(stress_new, 2)

# -------------------------------
# 📊 Enhanced Visualization Functions (Simplified)
# -------------------------------

class Visualizations:
    """Premium visualization functions"""
    
    @staticmethod
    def plot_wellness_journey(steps, euler_data, rk4_data, techniques):
        """Create a beautiful wellness journey visualization"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        x = range(steps + 1)
        
        # Anxiety plot
        ax1.plot(x, euler_data['anxiety'], 'o-', label='Euler Anxiety', linewidth=3, markersize=8,
                color='#FF6B6B', alpha=0.8, markerfacecolor='white')
        ax1.plot(x, rk4_data['anxiety'], 's-', label='RK4 Anxiety', linewidth=3, markersize=8,
                color='#4ECDC4', alpha=0.8, markerfacecolor='white')
        ax1.set_xlabel('Relaxation Steps', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Anxiety Level', fontsize=12, fontweight='bold')
        ax1.set_title('Anxiety Reduction Progress', fontsize=14, fontweight='bold')
        ax1.grid(True, alpha=0.2, linestyle='--')
        ax1.legend()
        
        # Add technique labels
        for i, tech in enumerate(techniques):
            if i < steps:
                ax1.annotate(f'Step {i+1}: {tech[:15]}...',
                            xy=(i+1, (euler_data['anxiety'][i+1] + rk4_data['anxiety'][i+1])/2),
                           xytext=(i+1, max(euler_data['anxiety'][i+1], rk4_data['anxiety'][i+1]) + 0.3),
                           ha='center', fontsize=8, alpha=0.7,
                           arrowprops=dict(arrowstyle='->', alpha=0.5))
        
        # Stress plot
        ax2.plot(x, euler_data['stress'], '^-', label='Euler Stress', linewidth=3, markersize=8,
                color='#FFA726', alpha=0.8, markerfacecolor='white')
        ax2.plot(x, rk4_data['stress'], 'v-', label='RK4 Stress', linewidth=3, markersize=8,
                color='#26C6DA', alpha=0.8, markerfacecolor='white')
        ax2.set_xlabel('Relaxation Steps', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Stress Level', fontsize=12, fontweight='bold')
        ax2.set_title('Stress Reduction Progress', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.2, linestyle='--')
        ax2.legend()
        
        plt.suptitle('Wellness Journey Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def create_report_card(person_id, initial, final, improvements, steps, best_method):
        """Create a SIMPLE premium report card"""
        fig = plt.figure(figsize=(12, 8))
        
        # Create grid
        gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
        
        # 1. Bar chart - Improvements
        ax1 = fig.add_subplot(gs[0, 0])
        categories = ['Anxiety', 'Stress', 'Total']
        anxiety_imp, stress_imp = improvements
        values = [anxiety_imp, stress_imp, anxiety_imp + stress_imp]
        colors = ['#FF6B6B', '#4ECDC4', '#8E44AD']
        
        bars = ax1.bar(categories, values, color=colors, edgecolor='black', linewidth=2)
        ax1.set_ylabel('Improvement (points)', fontsize=11, fontweight='bold')
        ax1.set_title('Improvement Summary', fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3, axis='y')
        
        for bar, value in zip(bars, values):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.07,
                    f'{value:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
        # 2. Donut chart - Initial vs Final
        ax2 = fig.add_subplot(gs[0, 1])
        initial_total = initial[0] + initial[1]
        final_total = final[0] + final[1]
        
        sizes = [initial_total, final_total]
        labels = ['Initial\nTotal Score', 'Final\nTotal Score']
        colors_donut = ['#E74C3C', '#2ECC71']
        
        wedges, texts, autotexts = ax2.pie(sizes, labels=labels, colors=colors_donut, autopct='%1.1f%%',
               startangle=90, wedgeprops=dict(width=0.4, edgecolor='black'))
        
        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontweight('bold')
            autotext.set_fontsize(10)
        
        for text in texts:
            text.set_fontsize(9)
            text.set_fontweight('bold')
        
        ax2.set_title('Total Wellness Score', fontsize=12, fontweight='bold')
        
        # 3. Progress comparison
        ax3 = fig.add_subplot(gs[1, 0])
        progress_data = {
            'Initial': [initial[0], initial[1]],
            'Final': [final[0], final[1]]
        }
        
        x = np.arange(2)
        width = 0.35
        
        bars1 = ax3.bar(x - width/2, progress_data['Initial'], width, label='Initial',
                       color=['#E74C3C', '#3498DB'], edgecolor='black')
        bars2 = ax3.bar(x + width/2, progress_data['Final'], width, label='Final',
                       color=['#FF6B6B', '#4ECDC4'], edgecolor='black')
        
        ax3.set_xlabel('Metrics', fontweight='bold')
        ax3.set_ylabel('Score', fontweight='bold')
        ax3.set_title('Before vs After Comparison', fontsize=12, fontweight='bold')
        ax3.set_xticks(x)
        ax3.set_xticklabels(['Anxiety', 'Stress'])
        ax3.legend()
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax3.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{height:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        # 4. Status indicators
        ax4 = fig.add_subplot(gs[1, 1])
        ax4.axis('off')
        
        # Calculate final status
        final_avg = (final[0] + final[1]) / 2
        
        if final_avg >= 8:
            status = "⚡ SEVERE"
            status_color = "#E74C3C"
            recommendation = "Urgent intervention needed"
        elif final_avg >= 6:
            status = "⚠️  HIGH"
            status_color = "#F39C12"
            recommendation = "Continue intensive program"
        elif final_avg >= 4:
            status = "📊 MODERATE"
            status_color = "#3498DB"
            recommendation = "Maintain current routine"
        else:
            status = "🌿 MILD"
            status_color = "#2ECC71"
            recommendation = "Wellness level good"
        
        status_text = f"""
        ┌──────────────────────────┐
        │      FINAL STATUS        │
        ├──────────────────────────┤
        │   Level: {status:^16} │
        │   Score: {final_avg:^16.1f} │
        └──────────────────────────┘
        
        Recommendation:
        {recommendation}
        
        Best Method: {best_method}
        Steps Completed: {steps}
        """
        
        ax4.text(0.1, 0.5, status_text, fontsize=11, va='center', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='#F8F9F9', alpha=0.9, edgecolor=status_color, linewidth=3))
        
        plt.suptitle(f'Premium Wellness Report - Person {person_id}', 
                     fontsize=16, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def method_comparison_chart(euler_improvements, rk4_improvements):
        """Create method comparison chart"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Bar chart comparison
        methods = ['Euler', 'RK4']
        anxiety_imps = [euler_improvements[0], rk4_improvements[0]]
        stress_imps = [euler_improvements[1], rk4_improvements[1]]
        
        x = np.arange(len(methods))
        width = 0.35
        
        bars1 = ax1.bar(x - width/2, anxiety_imps, width, label='Anxiety Improvement',
                        color='#FF6B6B', edgecolor='black')
        bars2 = ax1.bar(x + width/2, stress_imps, width, label='Stress Improvement',
                       color='#4ECDC4', edgecolor='black')
        
        ax1.set_xlabel('Method', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Improvement (points)', fontsize=12, fontweight='bold')
        ax1.set_title('Method Performance Comparison', fontsize=14, fontweight='bold')
        ax1.set_xticks(x)
        ax1.set_xticklabels(methods)
        ax1.legend()
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax1.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                        f'{height:.2f}', ha='center', va='bottom', fontsize=9)
        
        # Total improvement pie chart
        euler_total = euler_improvements[0] + euler_improvements[1]
        rk4_total = rk4_improvements[0] + rk4_improvements[1]
        
        sizes = [euler_total, rk4_total]
        labels = [f'Euler\n{euler_total:.2f}', f'RK4\n{rk4_total:.2f}']
        colors = ['#FFA726', '#26C6DA']
        
        ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
               startangle=90, explode=(0.05, 0.05), shadow=True)
        ax2.set_title('Total Improvement by Method', fontsize=14, fontweight='bold')
        
        plt.suptitle('Numerical Methods Comparison Analysis', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.show()

# -------------------------------
# 📈 Enhanced Data Analysis
# -------------------------------

class DataAnalyzer:
    """Enhanced data analysis functions"""
    
    @staticmethod
    def view_dataset_analysis(data):
        """Display comprehensive dataset analysis"""
        UI.print_header("DATASET ANALYSIS", "Comprehensive Wellness Metrics")
        
        # Basic Statistics
        UI.print_subheader("Basic Statistics")
        stats = {
            "Total Persons": len(data),
            "Avg Anxiety": f"{data['Initial_Anxiety'].mean():.2f}",
            "Avg Stress": f"{data['Initial_Stress'].mean():.2f}",
            "Max Anxiety": f"{data['Initial_Anxiety'].max():.2f}",
            "Min Anxiety": f"{data['Initial_Anxiety'].min():.2f}",
            "Max Stress": f"{data['Initial_Stress'].max():.2f}",
            "Min Stress": f"{data['Initial_Stress'].min():.2f}",
            "Std Anxiety": f"{data['Initial_Anxiety'].std():.2f}",
            "Std Stress": f"{data['Initial_Stress'].std():.2f}"
        }
        
        for key, value in stats.items():
            print(f"{Colors.BOLD}{key:20}{Colors.END}: {Colors.CYAN}{value}{Colors.END}")
        
        # Correlation Analysis
        UI.print_subheader("Correlation Analysis")
        correlation = data['Initial_Anxiety'].corr(data['Initial_Stress'])
        correlation_color = Colors.GREEN if correlation > 0.7 else Colors.YELLOW if correlation > 0.4 else Colors.RED
        print(f"{Colors.BOLD}Anxiety-Stress Correlation: {correlation_color}{correlation:.3f}{Colors.END}")
        
        if correlation > 0.7:
            print(f"{Colors.YELLOW}  ⓘ Strong positive correlation: High anxiety often accompanies high stress{Colors.END}")
        elif correlation > 0.4:
            print(f"{Colors.YELLOW}  ⓘ Moderate correlation: Anxiety and stress are somewhat related{Colors.END}")
        else:
            print(f"{Colors.YELLOW}  ⓘ Weak correlation: Anxiety and stress levels vary independently{Colors.END}")
        
        # Risk Assessment
        UI.print_subheader("Risk Assessment")
        high_risk = data[(data['Initial_Anxiety'] >= 8) | (data['Initial_Stress'] >= 8)]
        medium_risk = data[((data['Initial_Anxiety'] >= 6) & (data['Initial_Anxiety'] < 8)) |
                          ((data['Initial_Stress'] >= 6) & (data['Initial_Stress'] < 8))]
        low_risk = data[(data['Initial_Anxiety'] < 6) & (data['Initial_Stress'] < 6)]
        
        print(f"{Colors.RED}High Risk Persons: {len(high_risk)} ({len(high_risk)/len(data)*100:.1f}%){Colors.END}")
        print(f"{Colors.YELLOW}Medium Risk Persons: {len(medium_risk)} ({len(medium_risk)/len(data)*100:.1f}%){Colors.END}")
        print(f"{Colors.GREEN}Low Risk Persons: {len(low_risk)} ({len(low_risk)/len(data)*100:.1f}%){Colors.END}")
        
        # Ask for visualization
        print(f"\n{Colors.CYAN}{'─' * 50}{Colors.END}")
        choice = input(f"\n{Colors.BOLD}📊 Would you like to see visualizations? (y/n): {Colors.END}").lower()
        if choice == 'y':
            # Show simple visualization
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            
            # Anxiety histogram
            ax1.hist(data['Initial_Anxiety'], bins=15, color='#FF6B6B', alpha=0.7, edgecolor='black')
            ax1.axvline(data['Initial_Anxiety'].mean(), color='red', linestyle='--',
                        linewidth=2, label=f'Mean: {data["Initial_Anxiety"].mean():.2f}')
            ax1.set_xlabel('Anxiety Level', fontweight='bold')
            ax1.set_ylabel('Frequency', fontweight='bold')
            ax1.set_title('Anxiety Distribution', fontsize=13, fontweight='bold')
            ax1.grid(True, alpha=0.3)
            ax1.legend()
            
            # Stress histogram
            ax2.hist(data['Initial_Stress'], bins=15, color='#4ECDC4', alpha=0.7, edgecolor='black')
            ax2.axvline(data['Initial_Stress'].mean(), color='blue', linestyle='--',
                        linewidth=2, label=f'Mean: {data["Initial_Stress"].mean():.2f}')
            ax2.set_xlabel('Stress Level', fontweight='bold')
            ax2.set_ylabel('Frequency', fontweight='bold')
            ax2.set_title('Stress Distribution', fontsize=13, fontweight='bold')
            ax2.grid(True, alpha=0.3)
            ax2.legend()
            
            plt.suptitle('Dataset Analysis - Anxiety & Stress Distributions',
                         fontsize=14, fontweight='bold')
            plt.tight_layout()
            plt.show()

# -------------------------------
# 🎮 Main Application Class
# -------------------------------

class WellnessSimulator:
    """Main application class"""
    
    def __init__(self):
        self.data = self.load_dataset()
        self.current_session = None
    
    def load_dataset(self):
        """Load or create IMPROVED dataset"""
        UI.print_loading("Initializing wellness database")
        
        if not os.path.exists("anxiety_stress_data.csv"):
            UI.print_info("Creating realistic dataset...")
            np.random.seed(42)
            
            n_persons = 30
            # Create more realistic dataset
            # Beta distribution gives more realistic psychological distribution
            base_anxiety = np.random.beta(2, 3, n_persons) * 8 + 2  # Range: 2-10
            personality_factors = np.random.choice([0.8, 1.0, 1.2], n_persons)  # Stress multipliers
            base_stress = base_anxiety * personality_factors + np.random.normal(0, 0.8, n_persons)
            
            # Add therapeutic responsiveness (how well person responds to treatment)
            responsiveness = np.random.beta(3, 2, n_persons)  # Most people are responsive
            
            # Clip to valid range
            base_anxiety = np.clip(base_anxiety, 1, 10)
            base_stress = np.clip(base_stress, 1, 10)
            
            data = pd.DataFrame({
                'PersonID': range(1, n_persons + 1),
                'Initial_Anxiety': np.round(base_anxiety, 2),
                'Initial_Stress': np.round(base_stress, 2),
                'Responsiveness': np.round(responsiveness, 2)
            })
            data.to_csv("anxiety_stress_data.csv", index=False)
            UI.print_success(f"Created realistic dataset with {n_persons} persons")
        else:
            data = pd.read_csv("anxiety_stress_data.csv")
            # Add responsiveness column if not present (for backward compatibility)
            if 'Responsiveness' not in data.columns:
                data['Responsiveness'] = np.random.beta(3, 2, len(data)).round(2)
            UI.print_success(f"Loaded dataset with {len(data)} persons")
        
        return data
    
    def analyze_person(self):
        """Analyze a specific person with FIXED methods"""
        UI.print_header("PERSONAL WELLNESS ANALYSIS", "Deep Dive into Individual Metrics")
        
        while True:
            try:
                pid = int(input(f"\n{Colors.BOLD}🎯 Enter Person ID (1-{len(self.data)}): {Colors.END}"))
                if 1 <= pid <= len(self.data):
                    break
                UI.print_error(f"Please enter ID between 1-{len(self.data)}")
            except ValueError:
                UI.print_error("Please enter a valid number")
        
        person = self.data[self.data["PersonID"] == pid].iloc[0]
        anxiety0 = person["Initial_Anxiety"]
        stress0 = person["Initial_Stress"]
        responsiveness = person.get("Responsiveness", 0.7)
        
        # Display person card
        UI.person_card(pid, anxiety0, stress0, responsiveness)
        
        # Determine recommended steps
        avg = (anxiety0 + stress0) / 2
        if avg >= 8:
            max_steps = 5
            recommendation = "⚡ Severe levels detected - Intensive program (5 steps)"
            UI.print_warning(recommendation)
        elif avg >= 6:
            max_steps = 4
            recommendation = "⚠️  High levels - Extended program (4 steps)"
            UI.print_warning(recommendation)
        elif avg >= 4:
            max_steps = 3
            recommendation = "📊 Moderate levels - Standard program (3 steps)"
            UI.print_info(recommendation)
        else:
            max_steps = 2
            recommendation = "🌿 Mild levels - Light program (2 steps)"
            UI.print_success(recommendation)
        
        # Get steps
        while True:
            try:
                steps = int(input(f"\n{Colors.BOLD}🔄 Enter relaxation steps (1-{max_steps}): {Colors.END}"))
                if 1 <= steps <= max_steps:
                    break
                UI.print_error(f"Please enter between 1-{max_steps}")
            except ValueError:
                UI.print_error("Please enter a valid number")
        
        # Initialize simulation
        UI.print_header("WELLNESS JOURNEY", "Starting Relaxation Protocol")
        
        # Prepare techniques
        categories = list(relaxations.keys())
        selected_techniques = []
        for i in range(steps):
            category = categories[i % len(categories)]
            techs = relaxations[category]
            technique = techs[i % len(techs)]
            selected_techniques.append((category, technique))
        
        # Initialize both methods with same starting values
        a1, s1 = anxiety0, stress0  # Euler
        a2, s2 = anxiety0, stress0  # RK4
        
        # Store lists separately for each method
        a1_list, s1_list = [a1], [s1]
        a2_list, s2_list = [a2], [s2]
        
        # Simulate each step with FIXED methods
        for i in range(steps):
            category, technique = selected_techniques[i]
            
            UI.print_step(i + 1, steps, f"{technique} [{category}]")
            print(f"{Colors.CYAN}{'─' * 50}{Colors.END}")
            
            # FIXED: Apply methods with responsiveness factor
            a1_new, s1_new = WellnessModel.euler_method(a1, s1, category, responsiveness=responsiveness)
            a2_new, s2_new = WellnessModel.rk4_method(a2, s2, category, responsiveness=responsiveness)
            
            # Update values for next iteration
            a1, s1 = a1_new, s1_new
            a2, s2 = a2_new, s2_new
            
            # Store results
            a1_list.append(a1)
            s1_list.append(s1)
            a2_list.append(a2)
            s2_list.append(s2)
            
            # Display progress
            print(f"{Colors.GREEN}📊 Current State:{Colors.END}")
            print(f"{Colors.YELLOW}  Euler:{Colors.END}  Anxiety {a1_list[-2]:.2f} → {a1:.2f} "
                  f"| Stress {s1_list[-2]:.2f} → {s1:.2f}")
            print(f"{Colors.CYAN}  RK4:{Colors.END}    Anxiety {a2_list[-2]:.2f} → {a2:.2f} "
                  f"| Stress {s2_list[-2]:.2f} → {s2:.2f}")
            
            # Progress bar
            progress = ((i + 1) / steps) * 100
            bar_length = 30
            filled = int(bar_length * progress // 100)
            bar = f"{Colors.GREEN}{'█' * filled}{Colors.END}{'░' * (bar_length - filled)}"
            print(f"{Colors.BOLD}Overall Progress:{Colors.END} {bar} {progress:6.1f}%\n")
            
            time.sleep(0.5)
        
        # Calculate improvements correctly
        a1_red = anxiety0 - a1_list[-1]
        s1_red = stress0 - s1_list[-1]
        a2_red = anxiety0 - a2_list[-1]
        s2_red = stress0 - s2_list[-1]
        
        total1 = a1_red + s1_red
        total2 = a2_red + s2_red
        
        # Determine which method is better
        if total2 > total1:
            better = "RK4 Method"
            better_reason = "More accurate for coupled systems"
            best_improvements = (a2_red, s2_red)
            best_final = (a2_list[-1], s2_list[-1])
        else:
            better = "Euler Method"
            better_reason = "Simpler model works better for this case"
            best_improvements = (a1_red, s1_red)
            best_final = (a1_list[-1], s1_list[-1])
        
        UI.print_header("SESSION COMPLETE", "Wellness Journey Analysis")
        
        # Display final results
        print(f"\n{Colors.BOLD}🎯 Final Results:{Colors.END}")
        print(f"{Colors.CYAN}{'─' * 50}{Colors.END}")
        print(f"{Colors.YELLOW}Euler Method:{Colors.END}")
        print(f"  Anxiety Reduction: {Colors.GREEN}{a1_red:.2f} points{Colors.END}")
        print(f"  Stress Reduction:  {Colors.GREEN}{s1_red:.2f} points{Colors.END}")
        print(f"  Total Improvement: {Colors.BOLD}{Colors.GREEN}{total1:.2f} points{Colors.END}")
        
        print(f"\n{Colors.CYAN}RK4 Method:{Colors.END}")
        print(f"  Anxiety Reduction: {Colors.GREEN}{a2_red:.2f} points{Colors.END}")
        print(f"  Stress Reduction:  {Colors.GREEN}{s2_red:.2f} points{Colors.END}")
        print(f"  Total Improvement: {Colors.BOLD}{Colors.GREEN}{total2:.2f} points{Colors.END}")
        
        print(f"\n{Colors.BOLD}🏆 Best Performing Method: {Colors.CYAN}{better}{Colors.END}")
        print(f"{Colors.YELLOW}  Reason: {better_reason}{Colors.END}")
        
        # Mathematical comparison
        print(f"\n{Colors.BOLD}🧮 Numerical Analysis:{Colors.END}")
        print(f"{Colors.CYAN}{'─' * 50}{Colors.END}")
        
        # Calculate method accuracy (lower final score is better)
        euler_final_total = a1_list[-1] + s1_list[-1]
        rk4_final_total = a2_list[-1] + s2_list[-1]
        
        print(f"Euler Final Total Score: {euler_final_total:.2f}")
        print(f"RK4 Final Total Score:   {rk4_final_total:.2f}")
        
        if rk4_final_total < euler_final_total:
            print(f"{Colors.GREEN}✓ RK4 produces lower (better) final scores{Colors.END}")
        else:
            print(f"{Colors.YELLOW}✓ Euler produces lower (better) final scores{Colors.END}")
        
        # Improvement percentages
        anxiety_imp_percent = (best_improvements[0] / anxiety0) * 100
        stress_imp_percent = (best_improvements[1] / stress0) * 100
        total_imp_percent = ((best_improvements[0] + best_improvements[1]) / (anxiety0 + stress0)) * 100
        
        print(f"\n{Colors.BOLD}📊 Summary Metrics:{Colors.END}")
        print(f"{Colors.CYAN}{'─' * 60}{Colors.END}")
        print(f"Anxiety: {anxiety0:.1f} → {best_final[0]:.1f} ({best_improvements[0]:+.1f} points, {anxiety_imp_percent:+.1f}%)")
        print(f"Stress:  {stress0:.1f} → {best_final[1]:.1f} ({best_improvements[1]:+.1f} points, {stress_imp_percent:+.1f}%)")
        print(f"Total:   {anxiety0+stress0:.1f} → {best_final[0]+best_final[1]:.1f} ({best_improvements[0]+best_improvements[1]:+.1f} points, {total_imp_percent:+.1f}%)")
        print(f"{Colors.CYAN}{'─' * 60}{Colors.END}")
        
        # Store session data
        self.current_session = {
            'person_id': pid,
            'initial': (anxiety0, stress0),
            'final_euler': (a1_list[-1], s1_list[-1]),
            'final_rk4': (a2_list[-1], s2_list[-1]),
            'improvements_euler': (a1_red, s1_red),
            'improvements_rk4': (a2_red, s2_red),
            'steps': steps,
            'techniques': [t[1] for t in selected_techniques[:steps]],
            'best_method': better,
            'euler_data': {'anxiety': a1_list, 'stress': s1_list},
            'rk4_data': {'anxiety': a2_list, 'stress': s2_list}
        }
        
        return {
            'steps': steps,
            'euler_data': {'anxiety': a1_list, 'stress': s1_list},
            'rk4_data': {'anxiety': a2_list, 'stress': s2_list},
            'techniques': [t[1] for t in selected_techniques[:steps]]
        }
    
    def visualization_menu(self, session_data):
        """Display SIMPLIFIED visualization menu"""
        while True:
            UI.print_header("VISUALIZATION HUB", "Interactive Data Exploration")
            
            menu_options = [
                ("📈", "1", "Wellness Journey Dashboard"),
                ("📋", "2", "Report Card"),
                ("📊", "3", "Method Comparison"),
                ("🔙", "0", "Return to Main Menu")
            ]
            
            print(f"\n{Colors.BOLD}📊 Available Visualizations:{Colors.END}\n")
            print(f"{Colors.CYAN}{'┌' + '─' * 58 + '┐'}{Colors.END}")
            for icon, num, text in menu_options:
                print(f"{Colors.CYAN}{'│'}{Colors.END} {Colors.BOLD}{Colors.YELLOW}{num}.{Colors.END} {icon} {text:<50} {Colors.CYAN}{'│'}{Colors.END}")
            print(f"{Colors.CYAN}{'└' + '─' * 58 + '┘'}{Colors.END}")
            
            choice = input(f"\n{Colors.BOLD}🎨 Select visualization (0-3): {Colors.END}").strip()
            
            if choice == "0":
                UI.print_success("Returning to main menu...")
                break
            elif choice == "1":
                Visualizations.plot_wellness_journey(
                    session_data['steps'],
                    session_data['euler_data'],
                    session_data['rk4_data'],
                    session_data['techniques']
                )
            elif choice == "2" and self.current_session:
                # Use best method for report card
                if self.current_session['best_method'] == 'RK4 Method':
                    best_final = self.current_session['final_rk4']
                    best_improvements = self.current_session['improvements_rk4']
                else:
                    best_final = self.current_session['final_euler']
                    best_improvements = self.current_session['improvements_euler']
                
                Visualizations.create_report_card(
                    self.current_session['person_id'],
                    self.current_session['initial'],
                    best_final,
                    best_improvements,
                    self.current_session['steps'],
                    self.current_session['best_method']
                )
            elif choice == "3" and self.current_session:
                Visualizations.method_comparison_chart(
                    self.current_session['improvements_euler'],
                    self.current_session['improvements_rk4']
                )
            else:
                UI.print_error("Please select a valid option")
    
    def main_menu(self):
        """Display main menu"""
        while True:
            UI.clear_screen()
            UI.print_logo() 
            UI.print_header("MAIN NAVIGATION", "Wellness Analytics Platform")
            
            menu_options = [
                ("🔍", "1", "Personal Wellness Analysis"),
                ("📊", "2", "Dataset Analytics Dashboard"),
                ("👥", "3", "View All Persons Summary"),
                ("📈", "4", "Quick Statistics"),
                ("ℹ️", "5", "About & Help"),
                ("🚪", "0", "Exit Program")
            ]
            
            print(f"\n{Colors.BOLD}✨ Main Menu Options:{Colors.END}\n")
            for icon, num, text in menu_options:
                print(f"  {Colors.BOLD}{Colors.YELLOW}{num}.{Colors.END} {icon} {text}")
            
            choice = input(f"\n{Colors.BOLD}👉 Enter your choice (0-5): {Colors.END}").strip()
            
            if choice == "0":
                UI.print_header("THANK YOU", "For Using Our Wellness Platform")
                print(f"\n{Colors.GREEN}{Colors.BOLD}🌈 Stay Healthy, Stay Happy! 🌈{Colors.END}")
                print(f"{Colors.CYAN}👋 Goodbye! Take care of your mental wellness.{Colors.END}")
                break
            
            elif choice == "1":
                session_data = self.analyze_person()
                if session_data:
                    self.visualization_menu(session_data)
            
            elif choice == "2":
                DataAnalyzer.view_dataset_analysis(self.data)
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
            elif choice == "3":
                # View all persons summary
                UI.print_header("ALL PERSONS SUMMARY")
                print(f"\n{Colors.BOLD}Total Persons in Database: {Colors.CYAN}{len(self.data)}{Colors.END}")
                
                # Color-coded display
                print(f"\n{Colors.BOLD}{'ID':<5} {'Anxiety':<10} {'Stress':<10} {'Status':<15}{Colors.END}")
                print(f"{Colors.CYAN}{'─' * 45}{Colors.END}")
                
                for _, row in self.data.head(15).iterrows():
                    anxiety = row['Initial_Anxiety']
                    stress = row['Initial_Stress']
                    avg = (anxiety + stress) / 2
                    
                    if avg >= 8:
                        status = "SEVERE"
                        color = Colors.RED
                    elif avg >= 6:
                        status = "HIGH"
                        color = Colors.YELLOW
                    elif avg >= 4:
                        status = "MODERATE"
                        color = Colors.BLUE
                    else:
                        status = "MILD"
                        color = Colors.GREEN
                    
                    anxiety_color = Colors.ANXIETY_SEVERE if anxiety >= 8 else Colors.ANXIETY_HIGH if anxiety >= 6 else Colors.ANXIETY_MED if anxiety >= 4 else Colors.ANXIETY_LOW
                    stress_color = Colors.STRESS_SEVERE if stress >= 8 else Colors.STRESS_HIGH if stress >= 6 else Colors.STRESS_MED if stress >= 4 else Colors.STRESS_LOW
                    
                    print(f"{row['PersonID']:<5} {anxiety_color}{anxiety:<10.2f}{Colors.END} "
                          f"{stress_color}{stress:<10.2f}{Colors.END} {color}{status:<15}{Colors.END}")
                
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
            elif choice == "4":
                UI.print_header("QUICK STATISTICS")
                print(f"\n{Colors.BOLD}📊 Dataset Overview:{Colors.END}")
                print(f"{Colors.CYAN}{'─' * 40}{Colors.END}")
                print(f"{Colors.BOLD}Total Persons:{Colors.END} {Colors.CYAN}{len(self.data)}{Colors.END}")
                print(f"{Colors.BOLD}Average Anxiety:{Colors.END} {Colors.ANXIETY_MED}{self.data['Initial_Anxiety'].mean():.2f}{Colors.END}")
                print(f"{Colors.BOLD}Average Stress:{Colors.END} {Colors.STRESS_MED}{self.data['Initial_Stress'].mean():.2f}{Colors.END}")
                
                # Numerical methods comparison summary
                print(f"\n{Colors.BOLD}🧮 Numerical Methods Info:{Colors.END}")
                print(f"{Colors.CYAN}{'─' * 40}{Colors.END}")
                print(f"{Colors.YELLOW}Euler Method:{Colors.END} 1st order, simpler, faster but less accurate")
                print(f"{Colors.CYAN}RK4 Method:{Colors.END}     4th order, more accurate for coupled systems")
                print(f"{Colors.GREEN}Expected Result:{Colors.END} RK4 should generally perform better")
                
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")

            elif choice == "5":
                UI.print_header("ABOUT THIS PLATFORM")
                print(f"\n{Colors.BOLD}✨ Anxiety & Stress Dynamics Simulator v3.0{Colors.END}")
                print(f"{Colors.CYAN}{'─' * 50}{Colors.END}")
                print(f"{Colors.BOLD}🔹 Features:{Colors.END}")
                print(f"  • {Colors.GREEN}Advanced numerical models (Euler & RK4){Colors.END}")
                print(f"  • {Colors.GREEN}25+ relaxation techniques across 6 categories{Colors.END}")
                print(f"  • {Colors.GREEN}Interactive visualizations & dashboards{Colors.END}")
                print(f"  • {Colors.GREEN}Personalized wellness reports{Colors.END}")
                print(f"  • {Colors.GREEN}Risk assessment & correlation analysis{Colors.END}")
                print(f"\n{Colors.BOLD}🎯 Purpose:{Colors.END}")
                print(f"  {Colors.CYAN}To simulate and analyze anxiety/stress reduction through{Colors.END}")
                print(f"  {Colors.CYAN}various relaxation techniques using mathematical modeling.{Colors.END}")
                print(f"\n{Colors.BOLD}📊 How to use:{Colors.END}")
                print(f"  1. {Colors.YELLOW}Select 'Personal Wellness Analysis'{Colors.END}")
                print(f"  2. {Colors.YELLOW}Enter a Person ID (1-30){Colors.END}")
                print(f"  3. {Colors.YELLOW}Choose number of relaxation steps{Colors.END}")
                print(f"  4. {Colors.YELLOW}View results and visualizations{Colors.END}")
                print(f"\n{Colors.BOLD}👨‍💻 Developed by:{Colors.END} {Colors.YELLOW}Fahmida Akter{Colors.END}")
                input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
            
            else:
                UI.print_error("Invalid option. Please try again.")
                time.sleep(1)

            
       
# -------------------------------
# 🚀 Main Execution
# -------------------------------

if __name__ == "__main__":
    try:
        # Run the simulator
        simulator = WellnessSimulator()
        simulator.main_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}{Colors.BOLD}👋 Program interrupted. Goodbye!{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ An unexpected error occurred:{Colors.END}")
        print(f"{Colors.YELLOW}{str(e)}{Colors.END}")
        print(f"\n{Colors.CYAN}Please check your installation and try again.{Colors.END}")
    finally:
        print(f"\n{Colors.GREEN}{'═' * 60}{Colors.END}")
        print(f"{Colors.BOLD}{Colors.YELLOW}Thank you for using the Wellness Simulator! 🌈{Colors.END}")
        print(f"{Colors.GREEN}{'═' * 60}{Colors.END}")