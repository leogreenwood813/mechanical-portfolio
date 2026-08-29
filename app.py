from flask import Flask, render_template, abort

app = Flask(__name__)

profile = {
    "name": "Leo Greenwood",
    "email": "leogreenwood813@gmail.com",
    "linkedin": "https://www.linkedin.com/in/leo-greenwood-288032261",
    "github": "https://github.com/leogreenwood813",
    "bio" : "Mechanical Engineering student with a focus on iterative design, optimisation, and practical manufacturing. This portfolio showcases my ability to take a project from initial concept and research through to CAD modeling, FEA verification, physical prototyping and testing."
}

# ==============================================================================
# 1:8 SCALE MODEL CAR SECTIONS CONFIGURATION
# Modify titles, text, images, and subsection content directly below.
# ==============================================================================
scale_car_sections = {
    "section_1": {
        "title": "Section 1",
        "subtitle": "1:8 Scale Model Car ",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec1-1.png",
                "text": "coming soon"
            },
            {
                "title": "2. coming soon",
                "image": "car-sec1-2.png",
                "text": "coming soon"
            },
            {
                "title": "3. coming soon",
                "image": "car-sec1-3.png",
                "text": "coming soon"
            },
            {
                "title": "4. coming soon",
                "image": "car-sec1-4.png",
                "text": "coming soon."
            },
            {
                "title": "5. coming soon",
                "image": "car-sec1-5.png",
                "text": "coming soon."
            }
        ]
    },
    "section_2": {
        "title": "Section 2",
        "subtitle": "1:8 Scale Model Car",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec2-1.png",
                "text": "coming soon."
            },
            {
                "title": "2. coming soon",
                "image": "car-sec2-2.png",
                "text": "coming soon."
            },
            {
                "title": "3. coming soon",
                "image": "car-sec2-3.png",
                "text": "coming soon."
            },
            {
                "title": "4. coming soon",
                "image": "car-sec2-4.png",
                "text": "coming soon"
            },
            {
                "title": "5. coming soon",
                "image": "car-sec2-5.png",
                "text": "coming soon"
            }
        ]
    },
    "section_3": {
        "title": "Section 3",
        "subtitle": "1:8 Scale Model Car ",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec3-1.png",
                "text": "coming soon."
            },
            {
                "title": "2. coming soon",
                "image": "car-sec3-2.png",
                "text": "coming soon."
            },
            {
                "title": "3. coming soon",
                "image": "car-sec3-3.png",
                "text": "coming soon."
            },
            {
                "title": "4. coming soon",
                "image": "car-sec3-4.png",
                "text": "coming soon."
            },
            {
                "title": "5. coming soon",
                "image": "car-sec3-5.png",
                "text": "coming soon"
            }
        ]
    },
    "section_4": {
        "title": "Section 4",
        "subtitle": "1:8 Scale Model Car ",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec4-1.png",
                "text": "coming soon."
            },
            {
                "title": "2. coming soon",
                "image": "car-sec4-2.png",
                "text": "coming soon"
            },
            {
                "title": "3. coming soon",
                "image": "car-sec4-3.png",
                "text": "coming soon"
            },
            {
                "title": "4. coming soon",
                "image": "car-sec4-4.png",
                "text": "coming soon"
            },
            {
                "title": "5. coming soon",
                "image": "car-sec4-5.png",
                "text": "coming soon."
            }
        ]
    },
    "section_5": {
        "title": "Section 5",
        "subtitle": "1:8 Scale Model Car",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec5-1.png",
                "text": "coming soon."
            },
            {
                "title": "2. coming soon",
                "image": "car-sec5-2.png",
                "text": "coming soon."
            },
            {
                "title": "3. coming soon",
                "image": "car-sec5-3.png",
                "text": "coming soon."
            },
            {
                "title": "4. coming soon",
                "image": "car-sec5-4.png",
                "text": "coming soon."
            },
            {
                "title": "5. coming soon",
                "image": "car-sec5-5.png",
                "text": "coming soon."
            }
        ]
    },
    "section_6": {
        "title": "Section 6",
        "subtitle": "1:8 Scale Model Car ",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec6-1.png",
                "text": "coming soon"
            },
            {
                "title": "2. coming soon",
                "image": "car-sec6-2.png",
                "text": "coming soon"
            },
            {
                "title": "3. coming soon",
                "image": "car-sec6-3.png",
                "text": "coming soon."
            },
            {
                "title": "4. coming soon",
                "image": "car-sec6-4.png",
                "text": "coming soon."
            },
            {
                "title": "5. coming soon",
                "image": "car-sec6-5.png",
                "text": "coming soon."
            }
        ]
    },
    "section_7": {
        "title": "Section 7",
        "subtitle": "1:8 Scale Model Car",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec7-1.png",
                "text": "coming soon."
            },
            {
                "title": "2. coming soon",
                "image": "car-sec7-2.png",
                "text": "coming soon."
            },
            {
                "title": "3. coming soon",
                "image": "car-sec7-3.png",
                "text": "coming soon"
            },
            {
                "title": "4. coming soon",
                "image": "car-sec7-4.png",
                "text": "coming soon"
            },
            {
                "title": "5. coming soon",
                "image": "car-sec7-5.png",
                "text": "coming soon."
            }
        ]
    },
    "section_8": {
        "title": "Section 8",
        "subtitle": "1:8 Scale Model Car ",
        "sections": [
            {
                "title": "1. coming soon",
                "image": "car-sec8-1.png",
                "text": "coming soon."
            },
            {
                "title": "2. coming soon",
                "image": "car-sec8-2.png",
                "text": "coming soon."
            },
            {
                "title": "3. coming soon",
                "image": "car-sec8-3.png",
                "text": "coming soon"
            },
            {
                "title": "4. coming soon",
                "image": "car-sec8-4.png",
                "text": "coming soon."
            },
            {
                "title": "5. coming soon",
                "image": "car-sec8-5.png",
                "text": "coming soon."
            }
        ]
    }
}

projects_data = {
    "future": {
        "num": "001 / 006",
        "title": "🏎️ Upcoming: 1:8 Scale Model Car",
        "tag": "In Development",
        "date": "August 2026 - Current",
        "desc": "Coming soon.",
        "skills": ["Fusion 360", "Vehicle Dynamics", "FEA Analysis", "3D Printing", "Optimisation"],
        "is_coming_soon": False,
        "is_model_car_hub": True,
        
        # EDIT YOUR 8 VERTICAL BUTTON LABELS HERE
        "sub_sections": [
            {"id": "section_1", "label": "Section 1 "},
            {"id": "section_2", "label": "Section 2 "},
            {"id": "section_3", "label": "Section 3 "},
            {"id": "section_4", "label": "Section 4 "},
            {"id": "section_5", "label": "Section 5 "},
            {"id": "section_6", "label": "Section 6 "},
            {"id": "section_7", "label": "Section 7"},
            {"id": "section_8", "label": "Section 8 "}
        ]
    },
    "gearbox": {
        "num": "002 / 006",
        "title": "⚙️ EAPC Compliant Gearbox",
        "tag": "Academic Project",
        "date": "Oct 2025 - May 2026",
        "desc": "Designed, manufactured and tested an EAPC compliant gearbox. Researched gear mechanisms, used FEA to validate design choices, developed a functional design and optimised an arduino control system. Relevant to design engineering roles because it demonstrates mechanical research, structural validation, and systems integration.",
        "skills": ["Fusion 360", "AutoCAD", "FEA Static Stress", "Arduino (C++)", "Prototyping"],
        "is_coming_soon": False,
        
        "intro": "Following initial research, a range of potential configurations was developed, including multi-stage compound, belt-hybrid, and planetary gear sets. These concepts were evaluated using a decision matrix, with designs scored against criteria such as: maximum tooth stress, material efficiency, and manufacturing feasibility.",
        "cad_vs_prototype_narrative": "A final design was selected: a 3-stage compound gearbox achieving a 16.4:1 reduction ratio. The configuration features rotating shafts supported by bearings within the casing. Following CAD modeling (Figure 2a), DXF files were generated in AutoCAD to facilitate laser cutting. The components were then assembled into the final prototype (Figure 2b).",
        "fea_narrative": "FEA was conducted on all critical components to ensure structural integrity. Figure 3 illustrates the analysis performed on the gear teeth; loads were applied at the tooth tip to simulate a worst case scenario.. The analysis confirmed a maximum stress of 18.9 MPa, resulting in a safety factor exceeding the required 2.5 threshold. ",
        "video_narrative": "The prototype was then evaluated on a test rig, where initial testing revealed issues with chain tension and spline engagement. A failure was identified in the spline design: the initial profile was oriented for the incorrect freewheel direction, and when reversed, the extra clearance resulted in significant wobble under load. This was addressed by resizing the chain, redesigning the spline profile for correct engagement. These changes led to a significant performance increase, improving output from 22 to 77 revolutions during a 30-second interval.",
        "final_design_narrative": "The final design was manufactured to include protective casing around the sides and the motor. The arduino code was then optimised by altering the start up time and step up whilst still complying with EAPC regulations. Final testing outputted 95 revolutions during a 30 second interval. The design also demonstrated high material efficiency using only 2.5 out of 6 acrylic sheets, and prioritised assembly speed with a total fit-up time of 145 seconds to mount the gearbox and chain."
    },
    "suspension": {
        "num": "003 / 006",
        "title": "🏎️ Design and Optimisation of a Quarter Car Suspension System",
        "tag": "Personal Project",
        "date": "June 2026 - July 2026",
        "desc": "This project covers the design, simulation, and structural optimization of a quarter car suspension system. A 2-DOF state space model was developed in Python to simulate bump responses, extracting peak dynamic loads to inform CAD geometry and FEA loops. This project is relevant to vehicle dynamics, mechanical design, structural analysis, and system optimisation.",
        "skills": ["Python", "MATLAB", "Fusion 360", "FEA", "Topology Optimisation"],
        "is_coming_soon": False,
        "is_suspension": True,
        
        "python_code_url": "https://github.com/leogreenwood813/quarter-car-suspension-project/blob/main/Quarter_Car_Suspension_Code_Python.py",
        "matlab_code_url": "https://github.com/leogreenwood813/quarter-car-suspension-project/blob/main/Quarter_Car_Suspension_Code_MATLAB.m",
        "report_pdf_url": "suspension-report.pdf",
        "drawings_pack_url": "suspension-drawings.pdf",
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
                "image": "suspension-cad.jpg",
                "text": "Following the Python simulation, the components of the suspension system were then modelled using Fusion 360. This included components such as the upper and lower wishbones, chassis mounts, the knuckle, the spring-damper unit and the spindle. To ensure the CAD model matched the vehicle dynamics targets, the physical dimensions of the mechanical coil spring were calculated to achieve the required 11,000 N/m stiffness. Standard components such as the bolts and spherical rod ends were integrated directly from McMaster-Carr. Utilising datasheets and reference images, the custom knuckle, wishbones and the chassis mounts were modelled to ensure they fit the packaging constraints. These components were then made into an assembly."
            },
            {
                "title": "4. Full Suspension Assembly & Motion",
                "image": "suspension-assembly.mp4",
                "text": "The individual components were integrated into a final assembly to conduct a motion study to verify the assembly moved as intended and to check that the suspension components articulated correctly throughout the available travel. This completed assembly will then be utilised to conduct an FEA study across the 3 scenarios outlined in the Python simulation."
            },
            {
                "title": "5. FEA: Structural Analysis",
                "image": ["fea.png", "fea-zoomed.png"],
                "captions": ["Figure 5a: Equivalent Stress Contours (Baseline).", "Figure 5b: Critical Stress Concentration (Close-up)."],
                "text": "The wishbone geometry was imported into ANSYS Mechanical for static structural analysis. The peak shock force was applied to the upper mounting hole, with fixed supports bounding the spherical rod ends to simulate chassis mounting constraints. Initial simulation passes revealed severe stress concentrations localised on the rod end shafts. To ensure accuracy and properly capture these steep stress gradients, the mesh was refined to an element size of 2mm in this critical region. Because the baseline stresses drastically exceeded material yield limits, an iterative structural redesign was required."
            },
            {
                "title": "6. Iterative Redesign & Load Cases",
                "image": ["wishbone-redesign.png", "force-tables.png"],
                "captions": ["Figure 6a: Iterative Structural Redesign.", "Figure 6b: Resolved Boundary Force Envelopes."],
                "text": "To mitigate the critical stress concentrations, the assembly was redesigned with larger M14 spherical rod ends and thickened wishbone legs. The updated geometry was simulated across the three dynamic load cases mapped in Figure 6b. This structural intervention successfully reduced peak stresses and maximum displacements by approximately 2.7x across all scenarios, comfortably bringing the assembly within safe material yield limits and establishing a robust baseline for topology optimisation."
            },
            {
                "title": "7. Topology Optimisation",
                "image": "topology-optimisation.png",
                "text": "Topology optimisation was performed on the wishbone clevis using ANSYS Mechanical, configuring the solver to maximise global stiffness while reducing structural volume. Preservation constraints were applied to the mounting holes as material exclusion zones to maintain critical functional interfaces. Once the algorithm generated the primary load paths, the organic mesh was smoothed and imported into Fusion 360 to reconstruct clean, manufacturable CAD geometry."
            },
            {
                "title": "8. Mass Savings & Validation",
                "image": "mass-savings.png",
                "text": "The optimisation workflow yielded significant mass reductions across the entire suspension subsystem. Most notably, the upper wishbone clevis achieved the highest efficiency with a 41.19% material reduction. Conversely, because the upper wishbone legs had been widened during the initial redesign phase to handle peak stress concentrations, its subsequent optimisation yielded a more modest 4.87% mass saving. Despite these structural trade offs, the final assembly successfully shed weight while fully maintaining global assembly stiffness. "
            },
            {
                "title": "9. Conclusions",
                "image": "conclusion.PNG",  
                "text": "This project completed a full engineering design cycle for a lightweight double wishbone suspension corner. A 2-DOF Python simulation was used to evaluate three distinct operational scenarios. While Scenario 1 (minimising acceleration) compromised the car's track handling and Scenario 2 (minimising settling time) subjected the components to excessive structural stress, Scenario 3 was selected as the optimal, balanced compromise using a damping ratio of 0.636. The assembly was modelled in Fusion 360 to satisfy tight packaging constraints before undergoing structural analysis in ANSYS Mechanical. Following an iterative redesign to resolve critical joint bending moments, a final topology optimisation routine successfully stripped mass from low stress regions to achieve substantial weight savings while fully maintaining global assembly stiffness."
            }
        ]
    },
    "wing_mirror": {
        "num": "004 / 006",
        "title": "🚘 Aerodynamic Evolution of an Automotive Wing Mirror",
        "tag": "Personal Project",
        "date": "July 2026 - Aug 2026",
        "desc": "A comparative aerodynamic study evaluating 40 years of wing mirror design evolution between a 1980s baseline and a modern 2016 Corsa. Reverse engineered physical geometry using image calibration and 3D CAD modeling, validated assembly tolerances via 3D printing prototyping, and executed ANSYS Fluent CFD simulations to analyse flow fields and drag reduction across multiple highway speeds. Relevant to aerodynamic development, CAD modeling, and CFD validation. ",
        "skills": ["ANSYS Fluent (CFD)", "Fusion 360", "3D Printing", "Aerodynamics"],
        "is_coming_soon": False,
        "is_wing_mirror": True,
        
        "sections": [
            {
                "title": "1. Reference Capture & Blueprint Alignment",
                "image": ["wing-mirror-blueprint.png", "wing-mirror-photo.png"],
                "captions": ["Figure 1a: Blueprint of Wing Mirror.", "Figure 1b: Front View of Wing Mirror."],
                "text": "To reverse engineer the wing mirror geometry, photos were captured from key perspectives such as the front, rear, side, and top views. Lenses were aligned flat to the housing planes to minimise perspective distortion and optical parallax. Physical dimensions were recorded using digital calipers and a ruler to allow for calibration. Additional photos were taken of the A-pillar and lower casing to be used for reference. The images were imported into Fusion 360 as canvas planes and scaled using the recorded calliper measurements. These calibrated canvases were aligned across three orthographic planes to construct a blueprint, serving as the foundation for 3D surface reconstruction."
            },    
            {
                "title": "2. CAD Model",
                "image": "wing-mirror-cad.png",
                "text": "The CAD model was built in Fusion 360 using a combination of sketches, lofts, sweeps, and extrusions based on the calibrated images and measurements. The assembly was split into separate bodies to make it easier to 3D print, with internal alignment holes added to fit dowels for assembly. Because the physical mirror housing sits at a slight angle rather than a flat 90 degrees when extended, the side reference photo had slight perspective distortion along its depth. While the height calibration was accurate, relying solely on the photo projections caused alignment errors across planes. To resolve this, physical calliper measurements were taken across key reference points to manually correct the geometry and ensure the 3D model matched the real part."
            },
            {
                "title": "3. 3D Printed Model & Comparison",
                "image": ["wing-mirror-3dprint.png", "wing-mirror-comparison.jpg"],
                "captions": ["Figure 3a: 3D Printed Prototype.", "Figure 3b: Physical Prototype Comparison."],
                "text": "The mirror components were printed and assembled using 3D printed dowels for alignment. An initial 0.15 mm tolerance was chosen based on a separate tolerance gauge test. However, due to the small diameter of the dowels and holes, localised thermal shrinkage was higher than expected, causing a tight fit. Reducing the printed dowel diameter by an additional 0.10 mm resolved the fitment issue and allowed clean assembly. Part orientation was optimised to reduce overall print time, which created trade offs in surface finish. Rotating the A-pillar attachment section saved print hours but required print supports along a steep overhang, leaving noticeable layer marks and a rougher texture on that interface. While the internal geometry was simplified to avoid excessive modeling time, the external surfaces closely match the physical mirror, providing a solid baseline for the CFD fluid domain."
            },
            {
                "title": "4. CFD Analysis",
                "image": ["wing-mirror-cfd-old.png", "wing-mirror-cfd-new.png"],
                "captions": ["Figure 4a: 1980's CFD Pressure Contour Plot.", "Figure 4b: 2016 CFD Pressure Contour Plot."],
                "text": "Comparing the static pressure contours highlights how automotive wing mirror design has evolved over four decades. The older generation features a flat, boxy forward profile with sharp leading edges. This sharp transition forces incoming air to stall abruptly, resulting in a large high pressure area (the red region) across its front face and around its thick A-pillar mounting block. In contrast, the 2016 Corsa mirror uses rounded front faces and smooth, organic fillets. Air flows more easily around the housing, restricting the highest stagnation pressures to a much smaller region at the tip. However, the modern mirror is visibly deeper and thicker from front to back. This added depth is required to house internal electronics, such as motorised glass adjusters and heated element wiring, which were absent in older manual designs. Despite this increased depth and larger packaging envelope, the modern housing maintains a significantly cleaner aerodynamic profile by using smooth surface radii to keep the flow attached for longer before it detaches into the wake."
            },    
            {
                "title": "5. Conclusions & Validation",
                "image": "wing-mirror-results-table.png",
                "text": "Evaluating the numerical outputs reveals a dramatic performance gap between the two mirror generations. Total drag force increases quadratically with velocity for both models, rising from 0.370 N at 30 mph up to 1.869 N at 70 mph for the 2016 Corsa design. At a standard motorway cruising speed of 70 mph, the modern mirror reduces total drag force from 6.365 N down to 1.869 N, representing a 70.6% reduction in overall aerodynamic resistance compared to the 1980s baseline. Meanwhile, the calculated drag coefficient remains relatively stable across test speeds, maintaining values around 0.12 to 0.14 for the modern housing versus approximately 0.40 for the legacy model. This stability confirms that geometric shaping, rather than air velocity, is the primary driver of aerodynamic efficiency. Achieving a 70% reduction in drag force on an exterior component delivers a tangible real-world benefit. At motorway speeds, overcoming aerodynamic drag accounts for the majority of engine power output and fuel consumption. By smoothing the airflow over the housing, modern designs lower fuel consumption, reduce emissions, and suppress high-frequency wind noise caused by boundary layer separation right next to the driver's window. While these results clearly demonstrate the evolution of mirror styling, certain simulation limitations must be acknowledged. The standalone drag coefficients are noticeably lower than full-vehicle wind tunnel figures because the mirror was simulated in isolation within uniform freestream air. In practice, interaction drag caused by the side window boundary layer, the A-pillar vortex, and proximity to the door panel would increase the assembly's effective drag. Additionally, small geometric approximations made during photogrammetric reconstruction slightly simplify localized flow features. Despite these standalone testing constraints, the comparative trend remains fully valid and quantitatively proves the aerodynamic advantage of modern surface design."
            }    
        ]
    },
    "rocket": {
        "num": "005 / 006",
        "title": "🚀 Water Bottle Rocket Delivery System",
        "tag": "Academic Project",
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
        "num": "006 / 006",
        "title": "🚘 Spindle Design and Optimisation",
        "tag": "Personal Project",
        "date": "Oct 2025 - Oct 2025",
        "desc": "Designed a spindle based on technical drawings of a steering knuckle and wheel hub. Utilised FEA to evaluate performance under dynamic bump, braking, and cornering loads, optimising for stress concentrations and material selection. Relevant to design engineering roles by demonstrating proficiency in mechanical design optimisation and structural simulation.",
        "skills": ["Fusion 360", "CAD Optimisation", "BS 8888 Standards", "Material Selection"],
        "is_coming_soon": False,
        
        "base_analysis_narrative": "Initially, the spindle was modeled with an oversized flange-to-shaft transition (Figure 1a). FEA revealed peak stresses of 680 MPa at this interface (Figure 1b). Constructed from steel, this initial geometry presented significant manufacturability issues, including increased tool wear and large lead times, making the part costly to produce.",
        "iteration_narrative": "To address the initial manufacturability and cost constraints, the spindle was remodelled using aluminum. However, due to aluminum’s lower yield strength, this iteration failed to meet the required safety factor. The design was then reconfigured into a 2 part modular assembly (Figure 2a) where the shaft threads into the flange. While this reduced peak stress to 66MPa, peer review identified potential long term reliability concerns regarding stress concentration and fatigue at the thread interface. ",
        "final_redesign_narrative": "To resolve the reliability concerns associated with the modular assembly, the design was reverted to a single-part configuration. A step down diameter was introduced (70 mm - 40 mm - 25 mm). This geometry significantly reduced stress concentrations while improving manufacturability and cost efficiency compared to the earlier iterations."
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

@app.route("/project/future/<section_id>")
def scale_car_detail(section_id):
    section_data = scale_car_sections.get(section_id)
    if not section_data:
        abort(404)
    
    project = {
        "num": "001 / 006",
        "title": f"🏎️ {section_data['title']}",
        "tag": "In Development",
        "date": "July 2026 - Sept 2026",
        "is_coming_soon": False,
        "is_model_car_detail": True,
        "back_to_hub_url": "/project/future",
        "sections": section_data["sections"]
    }
    return render_template('project_detail.html', profile=profile, project=project)

if __name__ == '__main__':
    app.run(debug=True)