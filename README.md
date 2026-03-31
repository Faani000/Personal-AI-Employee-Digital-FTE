# Personal AI Employee – Gold Tier Hackathon Submission

## Student Name:

Farhan Ali

## Program:

PIAIC – AI / Agentic Engineering

## Project Title:

Personal AI Employee – Autonomous Digital FTE System

---

# Project Overview

This project demonstrates a simplified Digital FTE (Full-Time Employee) system that automates business task flow using Python agents and structured memory folders.

The system simulates how an AI employee can:

• Detect tasks
• Plan work
• Request approvals
• Execute actions
• Maintain logs
• Generate reports

---

# System Architecture

The system contains multiple AI agents:

1 Filesystem Watcher Agent
Detects new tasks and moves them into workflow.

2 Message Watcher Agent
Simulates external communication monitoring.

3 Agent Brain
Creates execution plans for tasks.

4 Approval Manager
Handles human-in-loop decision making.

5 Action Executor
Simulates MCP task execution.

6 Report Generator
Creates CEO level reports.

---

# Workflow Pipeline

Inbox → Needs_Action → Plans → Pending_Approval → Done

Rejected tasks go to Rejected folder.

All activity is recorded inside Logs.

Reports generated inside Reports folder.

---

# Technologies Used

Python
File System Automation
Multi-Agent Architecture
Structured Memory Design
Human Approval Workflow

---

# Key Features

Multi-Agent System
Task Lifecycle Management
Automated Planning
Approval Workflow
Activity Logging
CEO Reporting
Cross Domain Task Handling
Error Handling

---

# Gold Tier Requirements Covered

Multi Watchers ✔
Multi Agents ✔
Task Planning ✔
Human Approval ✔
Execution Layer ✔
Logging System ✔
Reporting System ✔
Structured Memory ✔
Cross Domain Tasks ✔

---

# How To Run

Open 5 terminals:

python filesystem_watcher.py

python message_watcher.py

python agent_core.py

python approval_manager.py

python action_executor.py

---

# Demo Steps

1 Start all agents
2 Add task in Inbox
3 Show automatic movement
4 Approve task
5 Show Done folder
6 Show Logs
7 Generate report

---

# Conclusion

This project demonstrates a basic autonomous Digital FTE system capable of handling structured business workflows with minimal human interaction.

Future improvements may include real LLM integration and API based execution.

---

END OF SUBMISSION
