import kagglehub
import pandas as pd
import os
import glob
from typing import List, Dict, Any

class ResearchDataLoader:
    def __init__(self):
        self.daily_dialog_path = None
        self.persona_chat_path = None

    def download_datasets(self):
        """Downloads the datasets using kagglehub as requested."""
        print("Downloading DailyDialog...")
        self.daily_dialog_path = kagglehub.dataset_download("thedevastator/dailydialog-unlock-the-conversation-potential-in")
        print("Path to DailyDialog:", self.daily_dialog_path)

        print("Downloading PersonaChat...")
        self.persona_chat_path = kagglehub.dataset_download("atharvjairath/personachat")
        print("Path to PersonaChat:", self.persona_chat_path)

    def load_daily_dialog(self, limit: int = 100) -> List[Dict[str, str]]:
        """Parses DailyDialog CSV files into a list of conversation turns."""
        if not self.daily_dialog_path:
            self.download_datasets()
        
        # Look for CSV files in the downloaded path
        csv_files = glob.glob(os.path.join(self.daily_dialog_path, "*.csv"))
        if not csv_files:
            return []
        
        # Load the first CSV for simplicity in research prototype
        df = pd.read_csv(csv_files[0])
        conversations = []
        
        # DailyDialog often has 'dialog' column with turns separated by __eou__
        for _, row in df.head(limit).iterrows():
            dialog = row.get('dialog', '')
            if isinstance(dialog, str):
                turns = dialog.split('__eou__')
                # Filter empty strings
                turns = [t.strip() for t in turns if t.strip()]
                conversations.append(turns)
        
        return conversations

    def load_persona_chat(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Parses PersonaChat into conversations."""
        if not self.persona_chat_path:
            self.download_datasets()
            
        # PersonaChat files are often in a specific format or CSV
        csv_files = glob.glob(os.path.join(self.persona_chat_path, "*.csv"))
        if not csv_files:
            return []
            
        df = pd.read_csv(csv_files[0])
        # Example processing for PersonaChat (adjust based on actual schema)
        # This is a generic placeholder for the trajectory
        return df.head(limit).to_dict('records')

if __name__ == "__main__":
    loader = ResearchDataLoader()
    loader.download_datasets()
    dialogs = loader.load_daily_dialog(5)
    print(f"Loaded {len(dialogs)} DailyDialog conversations.")
    for i, d in enumerate(dialogs):
        print(f"Conv {i+1}: {d[:2]}...")
