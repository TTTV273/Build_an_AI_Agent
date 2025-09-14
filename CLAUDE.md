# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Boot.dev course project for building an AI Agent - a toy version of Claude Code using Google's Gemini API. The project teaches how agentic AI tools work under the hood by creating a CLI agent that can perform coding tasks through function calling.

## Project Structure

- `CH1-LLMs/L1-Build_an_AI_Agent/` - Course lesson materials
  - `Lesson.md` - Main lesson content explaining the AI agent project

## Technologies

- Python 3.10+
- Google Gemini API (free tier)
- uv package manager
- Function calling for agent capabilities

## Agent Capabilities

The AI agent being built will have these core functions:
- Scan files in directories
- Read file contents
- Write/overwrite files
- Execute Python files
- Iterative task completion through function calls

## Development Commands

This project uses `uv` as the package manager. Common commands will be:
- `uv run main.py "task description"` - Run the agent with a task
- Boot.dev CLI tests for submission

## Course Context

This is part of Boot.dev's LLM course (Chapter 1, Lesson 1) focusing on building practical AI agents rather than training LLMs from scratch.