#!/usr/bin/env -S cargo -Zscript -q
---
[package]
edition = "2021"

[dependencies]
colored = "3.0.0"
rustyline = "15.0.0"
---

use std::{
    process::{Command, Stdio},
};
use rustyline::{Editor, Config, history::MemHistory};
use colored::*;

fn main() {
    println!("{}", 
        "Welcome to the REPL!"
            .bold()
            .white());
    let config = Config::builder().build();
    let history = MemHistory::new();
    let mut rl = Editor::<(), MemHistory>::with_history(config, history)
        .unwrap();

    loop {
        let readline = rl.readline(&format!("{} {}  ", 
            "seb-hyland/rosalind"
                .bold()
                .truecolor(50, 90, 220), 
            ">"
                .bold()
                .truecolor(128, 239, 128)));
        match readline {
            Ok(line) => {
                if line.trim() == "exit" { break; }
                parse_input(&line.trim());
                let _ = rl.add_history_entry(line.trim());
            },
            Err(_) => eprintln!("No input"),
        }
    }
}

fn parse_input(input: &str) {
    let output = Command::new("find")
        .arg(".")
        .arg("-path")
        .arg("./.git")
        .arg("-prune")
        .arg("-o")
        .arg("-type")
        .arg("f")
        .arg("-name")
        .arg(format!("*{input}*"))
        .arg("-print")
        .output()
        .unwrap();

    if output.status.success() {
        let found_file = output.stdout;
        let file_path = String::from_utf8_lossy(&found_file);
        let _ = Command::new("bat")
            .arg(file_path.trim())
            .stdout(Stdio::inherit())
            .output()
            .unwrap();
         
    } else {
        let stderr = String::from_utf8_lossy(&output.stderr);
        eprintln!("Error: {}", stderr);
    }
}

