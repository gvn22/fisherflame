from dedalus.tools import post
import pathlib

post.merge_process_files("analysis_tasks", cleanup=True)
set_paths = list(pathlib.Path("analysis_tasks").glob("analysis_tasks_s*.h5"))
post.merge_sets("analysis_tasks/analysis.h5", set_paths,cleanup=True)
