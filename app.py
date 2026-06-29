from flask import Flask, render_template, abort

app = Flask(__name__)

profile = {
    "name": "Leo Greenwood",
    "email": "leogreenwood813@gmail.com",
    "linkedin": "https://www.linkedin.com/in/leo-greenwood-288032261",
    "github": "https://github.com/your-username",
    "bio" : "Mechanical Engineering student with a focus on iterative design, optimisation, and practical manufacturing. This portfolio showcases my ability to take a project from initial concept and research through to CAD modeling, FEA verification, physical prototyping and testing."
}

projects_data = {
    "suspension": {
        "num": "001 / 005",
        "title": "🏎️ Design and Optimisation of a Quarter Car Suspension System",
        "tag": "Featured Project",
        "date": "June 2026 - Present",
        "desc": "This project covers the design, simulation, and structural optimization of a quarter car suspension system. A 2-DOF state space model was developed in Python to simulate bump responses, extracting peak dynamic loads to inform CAD geometry and FEA loops. This project is relevant to vehicle dynamics, mechanical design, structural analysis, and system optimisation.",
        "skills": ["Python", "MATLAB", "Fusion 360", "FEA", "Topology Optimisation"],
        "is_coming_soon": False,
        
        # Unique indicator for project_detail.html conditional rendering
        "is_suspension": True,
        
        # Python & MATLAB Code Links
        "python_code_url": "https://github.com/leogreenwood813/quarter-car-suspension-project/blob/main/Quarter_Car_Suspension_Code_Python.py",
        "matlab_code_url": "https://github.com/leogreenwood813/quarter-car-suspension-project/blob/main/Quarter_Car_Suspension_Code_MATLAB.m",
        "report_pdf_url": "suspension-report.pdf",
        # The distinct sequential sections with their text narratives and exact images
        "sections": [
            {
                "title": "1. Project Overview",
                "image": "suspension-flowchart.jpg",
                "text": "This chart shows the progression of the project from start to finish, demonstrating how loads from the python simulation directly inform the CAD geometry and FEA optimisation."
            },
            {
                "title": "2. Python Simulation",
                "image": "suspension-python-plots.png",
                "text": "Python was used to calculate the structural boundary conditions required to size and stress test the physical components of the suspension system. This was done by setting up a 2 DOF system to run flat road simulations before introducing an 80mm speed bump at 10m/s to evaluate maximum displacement, peak body acceleration, and mechanical travel limits. An iterative loop was then implemented across a range of damping ratios to extract settling times and accelerations against target criteria of less than 1 second and 0.3g respectively, allowing for the calculation of peak spring and damper forces. Because both criteria could not be met simultaneously, a compromise of three scenarios was decided: one minimising peak body acceleration, another minimising settling time, and a final one balancing the two. The spring and damper forces were then outputted at these three scenarios to directly drive the downstream CAD and FEA stages. This was then validated using a MATLAB code which outputted the exact same values."
            },   
            {
                "title": "3. Component CAD Modelling",
                "image": "suspension-cad.png",
                "text": "Coming Soon"
            },
            {
                "title": "4. Full Suspension Assembly & Motion",
                "image": "suspension-assembly.png",
                "text": "Coming Soon"
            },
            {
                "title": "5. FEA: Scenario 1 - Minimising Peak Body Acceleration",
                "image": "suspension-fea1.png",
                "text": "Coming Soon"
            },
            {
                "title": "6. FEA: Scenario 2 - Minimising Settling Time",
                "image": "suspension-fea2.png",
                "text": "Coming Soon"
            },
            {
                "title": "7. FEA: Scenario 3: Balanced Setup",
                "image": "suspension-fea3.png",
                "text": "Coming Soon"
            },
            {
                "title": "8. Topology Optimisation",
                "image": "suspension-topology.png",
                "text": "Coming Soon"
            },
            {
                "title": "9. Conclusions",
                "image": "conclusion.png",  
                "text": "Coming Soon (Project Report not yet completed)"
            }
        ]
    },
    "gearbox": {
        "num": "002 / 005",
        "title": "⚙️ EAPC Compliant Gearbox",
        "tag": "Featured Project",
        "date": "Oct 2025 - May 2026",
        "desc": "Designed, manufactured and tested an EAPC compliant gearbox. Researched gear mechanisms, used FEA to validate design choices, developed a functional design and optimised an arduino control system. Relevant to design engineering roles because it demonstrates mechanical research, structural validation, and systems integration.",
        "skills": ["Fusion 360", "AutoCAD" , "FEA Static Stress", "Arduino (C++)", "Prototyping"],
        "is_coming_soon": False,
        
        "intro": "Following initial research, a range of potential configurations was developed, including multi-stage compound, belt-hybrid, and planetary gear sets. These concepts were evaluated using a decision matrix, with designs scored against criteria such as: maximum tooth stress, material efficiency, and manufacturing feasibility.",
        "cad_vs_prototype_narrative": "A final design was selected: a 3-stage compound gearbox achieving a 16.4:1 reduction ratio. The configuration features rotating shafts supported by bearings within the casing. Following CAD modeling (Figure 2a), DXF files were generated in AutoCAD to facilitate laser cutting. The components were then assembled into the final prototype (Figure 2b).",
        "fea_narrative": "FEA was conducted on all critical components to ensure structural integrity. Figure 3 illustrates the analysis performed on the gear teeth; loads were applied at the tooth tip to simulate a worst case scenario.. The analysis confirmed a maximum stress of 18.9 MPa, resulting in a safety factor exceeding the required 2.5 threshold. ",
        "video_narrative": "The prototype was then evaluated on a test rig, where initial testing revealed issues with chain tension and spline engagement. A failure was identified in the spline design: the initial profile was oriented for the incorrect freewheel direction, and when reversed, the extra clearance resulted in significant wobble under load. This was addressed by resizing the chain, redesigning the spline profile for correct engagement. These changes led to a significant performance increase, improving output from 22 to 77 revolutions during a 30-second interval.",
        "final_design_narrative": "The final design was manufactured to include protective casing around the sides and the motor. The arduino code was then optimised by altering the start up time and step up whilst still complying with EAPC regulations. Final testing outputted 95 revolutions during a 30 second interval. The design also demonstrated high material efficiency using only 2.5 out of 6 acrylic sheets, and prioritised assembly speed with a total fit-up time of 145 seconds to mount the gearbox and chain."
    },
    "rocket": {
        "num": "003 / 005",
        "title": "🚀 Water Bottle Rocket Delivery System",
        "tag": "Featured Project",
        "date": "Feb 2025 - May 2025",
        "desc": "Designed, manufactured and tested a water bottle rocket delivery system, designed to carry medical supplies for flood relief operations. Utilised CFD to optimise nose cone geometry, validated findings through physical wind tunnel testing, and developed a MATLAB simulation to predict flight trajectories. Relevant to design engineering roles by demonstrating advanced aerodynamic analysis, simulation driven optimisation, and complex systems modeling.",
        "skills": ["ANSYS Fluent (CFD)", "MATLAB Simulation", "CNC Milling", "3D Printing"],
        "is_coming_soon": False,
        
        "intro": "ANSYS Fluent was used to analyse the flow over three distinct nose cone geometries at fixed initial conditions. Each simulation was executed to 100 iterations to ensure convergence, reliability and accuracy. For each geometry, the drag coefficient was calculated using the drag force generated by the simulation and the drag equation.",
        "cfd_narrative": "CFD analysis identified the hemispherical nose cone as the geometry with the minimum drag coefficient and highest aerodynamic efficiency. To ensure the reliability of these findings, a wind tunnel was used to validate the simulation results. The alignment between the CFD and experimental data confirmed the design's performance. Therefore, the hemispherical nose cone was selected for the final design.",
        "matlab_narrative": "A MATLAB simulation was developed to model the rocket’s flight across its thrust and free flight phases. The code implements an iterative numerical integration to account for variable mass, adiabatic air expansion and air resistance. This simulation was essential for calibrating launch pressure and water volume, ensuring all test flights landed within 2 meters of predicted targets.",
        "manufacturing_narrative": "The manufacturing strategy for the 3D-printed components and base connector was dictated by project requirements. However, laser cutting was selected for the fins to ensure symmetry and manufacturing repeatability. The CAD models for all 3D-printed assemblies were produced, and a lathe was used to manufacture the base connector. The CNC files were then made for the hole of the base connector to ensure high tolerance.",
        "final_assembly_narrative": "The final rocket design featured three fins for flight stability and a hemispherical nose cone for drag reduction. Initial testing identified instability in the launcher, which was addressed by reinforcing the launch slots and adopting a fixed 45-degree launch angle. The MATLAB code was used to calibrate the pressure and volume of water to reach a target horizontal distance of 70 metres. All three rockets launched successfully, reaching distances within 2 metres of the simulated distance."
    },
    "spindle": {
        "num": "004 / 005",
        "title": "🚘 Spindle Design and Optimisation",
        "tag": "Design & Optimisation",
        "date": "Oct 2025 - Oct 2025",
        "desc": "Designed a spindle based on technical drawings of a steering knuckle and wheel hub. Utilised FEA to evaluate performance under dynamic bump, braking, and cornering loads, optimising for stress concentrations and material selection. Relevant to design engineering roles by demonstrating proficiency in mechanical design optimisation and structural simulation.",
        "skills": ["Fusion 360", "CAD Optimisation", "BS 8888 Standards", "Material Selection"],
        "is_coming_soon": False,
        
        "base_analysis_narrative": "Initially, the spindle was modeled with an oversized flange-to-shaft transition (Figure 1a). FEA revealed peak stresses of 680 MPa at this interface (Figure 1b). Constructed from steel, this initial geometry presented significant manufacturability issues, including increased tool wear and large lead times, making the part costly to produce.",
        "iteration_narrative": "To address the initial manufacturability and cost constraints, the spindle was remodelled using aluminum. However, due to aluminum’s lower yield strength, this iteration failed to meet the required safety factor. The design was then reconfigured into a 2 part modular assembly (Figure 2a) where the shaft threads into the flange. While this reduced peak stress to 66MPa, peer review identified potential long term reliability concerns regarding stress concentration and fatigue at the thread interface. ",
        "final_redesign_narrative": "To resolve the reliability concerns associated with the modular assembly, the design was reverted to a single-part configuration. A step down diameter was introduced (70 mm - 40 mm - 25 mm). This geometry significantly reduced stress concentrations while improving manufacturability and cost efficiency compared to the earlier iterations."
    },
    "future": {
        "num": "005 / 005",
        "title": "✨ Future Project Showcase",
        "tag": "Coming Summer 2026",
        "date": "July 2026 - Sept 2026",
        "desc": "This slot is reserved for my upcoming summer engineering projects and structural optimisation models. Stay tuned for deeper dives into mechanical design iterations.",
        "skills": ["Fusion 360", "CAD Optimisation", "Advanced Modeling"],
        "is_coming_soon": True,
        "full_details": "Coming soon."
    }
}

@app.route("/")
def home():
    return render_template('index.html', profile=profile)

@app.route("/projects")
def projects_hub():
    return render_template('projects.html', profile=profile, projects=projects_data)

@app.route("/project/<project_id>")
def project_detail(project_id):
    project = projects_data.get(project_id)
    if not project:
        abort(404)
    return render_template('project_detail.html', profile=profile, project=project)

if __name__ == '__main__':
    app.run(debug=False)