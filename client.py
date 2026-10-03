"""Interactive Product Tour Qualification Dialogue Engine.
100% Python Standard Library.
"""

class ProductTourDialogueEngine:
    """Conducts conversational qualification, dynamically tailoring step-by-step tour paths."""
    
    @staticmethod
    def compute_tour_path(user_response: dict) -> dict:
        role = user_response.get("user_role", "evaluator").lower()
        primary_goal = user_response.get("goal", "general_productivity").lower()
        team_size = user_response.get("team_size", 1)
        
        recommended_tracks = []
        if "dev" in role or "engineer" in role or "cto" in role:
            recommended_tracks.append({
                "module": "API & MCP Tool Integration",
                "focus": "Automated function calling, schema validation, and SDK client integration.",
                "duration_minutes": 4
            })
            recommended_tracks.append({
                "module": "Local Debugging & Sandboxing",
                "focus": "Running agents in isolated local runtimes with zero cloud dependencies.",
                "duration_minutes": 3
            })
        elif "product" in role or "founder" in role or "business" in role:
            recommended_tracks.append({
                "module": "Growth & Autonomous Funnel Setup",
                "focus": "Outreach personalization, interactive demos, and ROI tracking dashboards.",
                "duration_minutes": 5
            })
            recommended_tracks.append({
                "module": "Multi-Channel Agent Collaboration",
                "focus": "Integrating agents directly into team Slack and Discord workspaces.",
                "duration_minutes": 3
            })
        else:
            recommended_tracks.append({
                "module": "Quickstart Interactive Walkthrough",
                "focus": "Standard end-to-end tour highlighting key agent features in under 3 minutes.",
                "duration_minutes": 3
            })
            
        custom_followup_question = (
            "Would you like us to configure sample API endpoints for your engineering team, "
            "or do you want to explore the visual workspace first?"
        )
        
        return {
            "qualification_profile": {"role": role, "goal": primary_goal, "team_size": team_size},
            "tailored_track_count": len(recommended_tracks),
            "tracks": recommended_tracks,
            "suggested_dialogue_prompt": custom_followup_question
        }
