import sqlite3
import json
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class DatabaseManager:
    db_path: str = "biosearchx.db"

    def __init__(self):
        self._init_db()

    def _init_db(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Sequences table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sequences (
                id TEXT PRIMARY KEY,
                seq TEXT NOT NULL,
                type TEXT NOT NULL,
                organism TEXT,
                annotations TEXT,
                metadata TEXT
            )
        ''')
        
        # Variants table for clinical data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS variants (
                chrom TEXT,
                pos INTEGER,
                ref TEXT,
                alt TEXT,
                significance TEXT,
                evidence TEXT,
                PRIMARY KEY (chrom, pos, ref, alt)
            )
        ''')
        
        conn.commit()
        conn.close()

    def add_sequence(self, sequence: Dict):
        """Add a sequence to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO sequences 
            (id, seq, type, organism, annotations, metadata)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            sequence.get("id"),
            sequence.get("seq"),
            sequence.get("type"),
            sequence.get("organism"),
            json.dumps(sequence.get("annotations", {})),
            json.dumps(sequence.get("metadata", {}))
        ))
        conn.commit()
        conn.close()
