# 📁 Course Folder Structure Documentation

## 🎯 Overview

This document outlines the complete folder structure for SE 444: Introduction to Artificial Intelligence course materials. The structure is designed to be modular, scalable, and easy to navigate for both instructors and students.

---

## 📚 **Current Implementation** (Weeks 1-3 + Syllabus)

```
introduction_to_ai_course/
├── 📄 README.md
├── 📄 LICENSE
├── 🔧 update_repo.sh
├── 📄 FOLDER_STRUCTURE.md
├── 📁 lectures/
│   ├── 📁 week01_intro_and_agents/
│   │   ├── 📁 slides/
│   │   │   ├── 📄 01_introduction_to_ai.pdf
│   │   │   └── 📄 02_intelligent_agents.pdf
│   │   ├── 📁 labs/
│   │   │   ├── 📄 lab01_setup_environment.md
│   │   │   └── 📁 code/
│   │   ├── 📁 exercises/
│   │   │   ├── 📄 exercises_week01.md
│   │   │   └── 📄 practice_problems.md
│   │   ├── 📁 solutions/
│   │   │   ├── 📄 lab_solutions.md
│   │   │   └── 📄 exercise_solutions.md
│   │   ├── 📁 resources/
│   │   │   ├── 📄 additional_readings.md
│   │   │   ├── 📄 videos_links.md
│   │   │   └── 📁 demos/
│   │   └── 📄 README.md
│   └── 📁 week02-03_search_algorithms/
│       ├── 📁 slides/
│       │   ├── 📄 01_problem_formulation.pdf
│       │   ├── 📄 02_uninformed_search_bfs_dfs.pdf
│       │   ├── 📄 03_uniform_cost_search.pdf
│       │   ├── 📄 04_informed_search_greedy_astar.pdf
│       │   └── 📄 05_heuristics.pdf
│       ├── 📁 labs/
│       │   ├── 📁 week02_uninformed_search/
│       │   │   ├── 📄 bfs_dfs_implementation.md
│       │   │   └── 📁 code/
│       │   └── 📁 week03_informed_search/
│       │       ├── 📄 astar_implementation.md
│       │       └── 📁 code/
│       ├── 📁 exercises/
│       │   ├── 📄 search_problems_uninformed.md
│       │   ├── 📄 search_problems_informed.md
│       │   └── 📄 heuristic_design_exercises.md
│       ├── 📁 solutions/
│       │   ├── 📄 lab_solutions_week02.md
│       │   ├── 📄 lab_solutions_week03.md
│       │   └── 📄 exercise_solutions.md
│       ├── 📁 resources/
│       │   ├── 📄 search_visualization_tools.md
│       │   ├── 📄 additional_algorithms.md
│       │   └── 📁 demos/
│       └── 📄 README.md
└── 📁 syllabus/
    ├── 📄 course_outline.md
    ├── 📄 grading_policy.md
    ├── 📄 schedule.md
    └── 📄 policies.md
```

---

## 🔮 **Future Implementation** (Complete Structure)

### 📚 **Remaining Lecture Weeks**
```
lectures/ (continued)
├── 📁 week04_local_search/
├── 📁 week05_constraint_satisfaction/
├── 📁 week06_midterm1_review/
├── 📁 week07_propositional_logic/
├── 📁 week08_first_order_logic/
├── 📁 week09_planning/
├── 📁 week10_probability_bayes/
├── 📁 week11_midterm2_review/
├── 📁 week12_bayesian_networks/
├── 📁 week13_multiagent_systems/
├── 📁 week14_break/
├── 📁 week15_ai_ethics_safety/
├── 📁 week16_projects/
└── 📁 week17_presentations/
```

### 📝 **Assessment Folders**
```
├── 📁 assignments/
│   ├── 📁 assignment01_search_algorithms/
│   ├── 📁 assignment02_csp/
│   ├── 📁 assignment03_logic/
│   ├── 📁 assignment04_probability/
│   └── 📁 assignment05_multiagent/
├── 📁 quizzes/
│   ├── 📁 quiz01_search_algorithms/
│   └── 📁 quiz02_logic_planning/
├── 📁 exams/
│   ├── 📁 midterm01/
│   ├── 📁 midterm02/
│   └── 📁 final_exam/
```

### 🚀 **Project & Resource Folders**
```
├── 📁 projects/
│   └── 📁 final_project/
├── 📁 code_examples/
│   ├── 📁 search_algorithms/
│   ├── 📁 logic_systems/
│   ├── 📁 probability_demos/
│   └── 📁 ai_agents/
├── 📁 datasets/
│   ├── 📁 search_problems/
│   ├── 📁 classification_data/
│   └── 📁 game_scenarios/
└── 📁 tools/
    ├── 📁 visualizations/
    ├── 📁 simulators/
    └── 📁 utilities/
```

---

## 🏗️ **Structure Design Principles**

### 📚 **Weekly Lecture Organization**
Each lecture week follows a consistent structure:
- **📊 slides/**: PDF presentations and lecture materials
- **💻 labs/**: Hands-on coding exercises with starter code
- **📝 exercises/**: Practice problems and theoretical exercises  
- **✅ solutions/**: Complete solutions for labs and exercises
- **📖 resources/**: Additional readings, videos, and demo materials
- **📄 README.md**: Week overview and learning objectives

### 🎯 **Key Features**

#### **🔍 Unified Search Module (Weeks 2-3)**
- Combines uninformed and informed search in one comprehensive module
- Progressive learning from basic to advanced search algorithms
- Week-specific lab divisions while maintaining conceptual unity

#### **📝 Assessment Integration**
- Clear separation between assignments, quizzes, and exams
- Each assessment includes rubrics and solutions
- Sample problems and practice materials included

#### **🛠️ Reusable Resources**
- **code_examples/**: Reusable implementations across topics
- **datasets/**: Sample data for exercises and projects  
- **tools/**: Visualization and simulation utilities

---

## 📋 **Implementation Timeline**

### ✅ **Phase 1: Core Structure** (Current)
- [x] Week 1: Introduction and Agents
- [x] Week 2-3: Search Algorithms (Combined)
- [x] Syllabus materials
- [x] Basic repository setup

### 🔄 **Phase 2: Mid-Course** (Next)
- [ ] Weeks 4-6: Local Search, CSP, Midterm 1
- [ ] Assignment templates and rubrics
- [ ] Quiz materials

### 🚀 **Phase 3: Advanced Topics** (Future)
- [ ] Weeks 7-11: Logic, Planning, Probability
- [ ] Weeks 12-17: Advanced topics and projects
- [ ] Complete assessment suite
- [ ] Tool and dataset integration

---

## 📊 **Folder Naming Conventions**

| **Type** | **Format** | **Example** |
|----------|------------|-------------|
| Week Folders | `weekXX_topic_name` | `week01_intro_and_agents` |
| Combined Weeks | `weekXX-YY_topic_name` | `week02-03_search_algorithms` |
| Assignments | `assignmentXX_topic` | `assignment01_search_algorithms` |
| Slides | `XX_descriptive_name.pdf` | `01_introduction_to_ai.pdf` |
| Labs | `lab_descriptive_name.md` | `lab01_setup_environment.md` |

---

## 🔧 **Maintenance Notes**

- Each week folder should have a README.md with learning objectives
- Solutions should be in separate folders to control access
- Use consistent file naming across all weeks
- Update this documentation when adding new weeks or changing structure
- Maintain the update_repo.sh script for easy GitHub synchronization

---

*Last Updated: January 2025*
*Version: 1.0*
