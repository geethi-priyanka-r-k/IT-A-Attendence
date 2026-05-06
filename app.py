import streamlit as st

st.set_page_config(page_title="IT-A Attendance", page_icon="📋", layout="centered")

# Data Mapping
students = {
    1:"AARTHI A", 2:"AKSHAYA R S", 3:"AMIRTHA S", 4:"ANEESHA P",
    5:"ARDHANARI L", 6:"BALABHARATHI S", 7:"BALAJI S R",
    8:"BARANIDHARAN S", 9:"BHOOMIKA D", 10:"BOOPATHI RAJA P",
    11:"CHANDRA KRISHNAN D", 12:"CHANDRU E", 13:"DEEPAK M",
    14:"DEEPANRAJ B", 15:"DEVAPRAKASH S", 16:"DEVIPRIYA D",
    17:"DEVISHIRINI S", 18:"DHANUSH KUMAR S", 19:"DHARANESH P",
    20:"DHARANIDHARAN M", 21:"DHARSAN R", 22:"DHARSHANA R",
    23:"DHARSHINI M", 24:"DHARSHINI T", 25:"DHARUN M",
    26:"DHESIKAA V", 27:"DIVAKARAN S", 28:"DURAIAKASH S",
    29:"DURAIMURUGAN R", 30:"FRANCISCA MARY A",
    31:"GANDHISELVAN P", 32:"GEETHA ARUN PRIYA S B",
    33:"GEETHI PRIYANKA R K", 34:"GOMATHI SANKAR M",
    35:"GOPIKA V", 36:"GOWTHAM A", 37:"HAREESH T",
    38:"HARINA SHRI S", 39:"HARSHANTH V", 40:"IMRAN KHAN M",
    41:"INBARAGAVAN P", 42:"JAGADEESAN K",
    43:"JEETHENDRABABU P", 44:"JEEVAN S",
    45:"JOHN BRIGHTSON N", 46:"KALKI R", 47:"KANISHKA P",
    48:"KARTHIGA SREE SURESH", 49:"KARTHIK A",
    50:"KAVIYA A", 51:"KAVIYASRI R", 52:"KEERTHIK T",
    53:"KEERTHIVARSHINI C", 54:"KISHOR K",
    55:"LAKSHANA S", 56:"LAKSHANIKA M K S",
    57:"LALITH KUMAR V", 58:"LOGITH PRASATH R S",
    59:"MADHAN M", 60:"MALARAVAN S",
    301:"ABISHEK K S", 302:"FARHATHMANAS U",
    303:"KEERTHI VARMA S", 304:"MOHAMED SAALIM C K A"
}

st.title("📋 IT-A Attendance")
st.markdown("---")

input_data = st.text_area(
    "Enter Register Numbers",
    placeholder="Example: 33,1,45",
    height=150
)

st.write("")

if st.button("Generate Attendance", use_container_width=True, type="primary"):
    if input_data.strip():
        raw_numbers = [num.strip() for num in input_data.split(',')]
        
        output_lines = []
        valid_idx = 1
        
        for num_str in raw_numbers:
            if not num_str:
                continue
                
            try:
                num = int(num_str)
                formatted_num = f"{num:02d}" if num < 100 else str(num)
                
                if num in students:
                    output_lines.append(f"{valid_idx}. {students[num]} ({formatted_num})")
                else:
                    output_lines.append(f"{valid_idx}. Unknown ({formatted_num})")
                    
            except ValueError:
                output_lines.append(f"{valid_idx}. Unknown ({num_str})")
                
            valid_idx += 1
            
        if output_lines:
            st.markdown("### Output")
            final_output = "\n".join(output_lines)

            # Show output (editable)
            st.text_area(
                "Result",
                value=final_output,
                height=min(300, len(output_lines) * 30 + 50),
                label_visibility="collapsed"
            )

            # ✅ COPY BUTTON (native Streamlit)
            st.markdown("#### 📋 Copy Attendance")
            st.code(final_output, language="text")
