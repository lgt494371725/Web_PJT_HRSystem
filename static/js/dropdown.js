function createDropdown(data, dropdownId, placeholder = '選択してください') {
    $(dropdownId).empty();
    $(dropdownId).select2({
        data: data,
        placeholder: placeholder,
        allowClear: true,
        closeOnSelect: true
    });
    
    $(dropdownId).val(null).trigger('change');
    }

function setSkillDropdown(selectComponentId) {
    $.ajax({
        url: "/hr_tool/all_skills/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'スキルを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}


function setSkillCategoriesDropdown(selectComponentId) {
    $.ajax({
        url: "/hr_tool/all_skillCategories/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'スキルカテゴリを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}

function setCareerLevelsDropdown(selectComponentId) {
    $.ajax({
        url: "/hr_tool/all_careerLevels/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'キャリアレベルを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}


function setIndustriesDropdown(selectComponentId) {
    $.ajax({
        url: "/hr_tool/all_industries/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'インダストリーを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}

function setHomeofficesDropdown(selectComponentId) {
    $.ajax({
        url: "/hr_tool/all_homeoffices/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'ホームオフィスを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}

function setDtesDropdown(selectComponentId) {
    $.ajax({
        url: "/hr_tool/all_dtes/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'DTEを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}


function setSkillInCategoriesDropdown(selectComponentId,categoryId = null) {
    if(categoryId ==null){
        createDropdown([], selectComponentId, placeholder = 'スキルカテゴリを選択してください')
        return
    }
    $.ajax({
        url: "/hr_tool/skills_in_categories/ + categoryId",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        let dropdownData = data.map(d => ({ id: d.id, text: d.name }));
        console.log(dropdownData)
        createDropdown(dropdownData, selectComponentId, placeholder = 'スキルを選択してください');
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
}





