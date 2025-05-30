from flask import Blueprint, render_template, request, redirect, url_for
from .services import llm_service # Import the llm_service module

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 1. Retrieval of form data
        project_description = request.form.get('project_description')
        location_data = request.form.get('location_data')
        policy_documents_file = request.files.get('policy_documents') # Example: FileStorage object
        community_feedback = request.form.get('community_feedback')

        # Placeholder for processed results
        results = {}
        report_summary = "Processing..."

        # 2. Logic for selecting appropriate LLM tools based on input
        # This is a simplified example. A real app might have more complex logic,
        # allow users to select tools, or run a predefined pipeline.

        if project_description:
            # 3. Calling placeholder functions in llm_service.py
            results['project_analysis'] = llm_service.analyze_project_description(project_description)

        if location_data:
            results['location_processing'] = llm_service.process_location_data(location_data)

        if policy_documents_file and policy_documents_file.filename != '':
            # In a real app, you'd save the file or process its stream.
            # For now, we'll just pass a representation (e.g., filename or mock object)
            # to the service layer. For this example, passing the FileStorage object.
            results['policy_summary'] = llm_service.summarize_policy_documents([policy_documents_file])

        if community_feedback:
            results['feedback_interpretation'] = llm_service.interpret_community_feedback(community_feedback)

        # Consolidate results and generate a final report (simplified)
        if results:
            report_summary = llm_service.compile_planning_report(results)

        # 4. Handling the response from the LLM service
        # For now, we'll just pass the raw results and summary to the template.
        # A real app would likely format this nicely or redirect to a results page.
        return render_template('index.html', results=results, report_summary=report_summary, form_submitted=True)

    # For GET request
    return render_template('index.html', form_submitted=False)
