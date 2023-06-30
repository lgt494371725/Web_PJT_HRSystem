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


function setupColumnFilters(settings) {
    settings.api().columns().every(function () {
        let column = this;

        let filterIcon = $(`<i class="fas fa-filter" style="cursor:pointer; font-size: 0.8em; margin-left: 4px;"></i>`);
        let header = $(column.header());
        header.css('white-space', 'nowrap');
        header.append(filterIcon);

        let dropdownMenu = $(
            `<div class="dropdown-menu" style="position: absolute; z-index: 1050;">
            <a class="dropdown-item" href="#">All</a>
            </div>`
        ).appendTo('body');

        column.data().unique().sort().each(function (d, j) {
            dropdownMenu.append('<a class="dropdown-item" href="#">' + d + '</a>');
        });

        filterIcon.on('click', function (event) {
            event.stopPropagation();
            dropdownMenu.css({
                display: 'block',
                top: filterIcon.offset().top + filterIcon.outerHeight(),
                left: filterIcon.offset().left
            });
        });

        dropdownMenu.on('click', '.dropdown-item', function (event) {
            event.preventDefault();
            let val = $.fn.dataTable.util.escapeRegex($(this).text());
            column.search(val !== 'All' ? '^' + val + '$' : '', true, false).draw();
            dropdownMenu.hide();

            if (val !== 'All') {
                filterIcon.addClass('filter-active');
            } else {
                filterIcon.removeClass('filter-active');
            }
        });

        $(document).on('click', function (event) {
            if (!filterIcon.is(event.target) && filterIcon.has(event.target).length === 0 &&
                !dropdownMenu.is(event.target) && dropdownMenu.has(event.target).length === 0) {
                dropdownMenu.hide();
            }
        });
    });
 }


function createTable(data, tableId, detailUrl = null) {
        // Destroy the table if it already exists
        if ($.fn.DataTable.isDataTable(tableId)) {
            $(tableId).DataTable().destroy();
        }
        //Get the column names from the data.
        let columns = [];
        if (data && data.length > 0) {
            columns = Object.keys(data[0]).map(key => {
                // Hide the id column
                console.log(key)
                if (key === 'id' || key === '社員番号') {
                    if (detailUrl) {
                        console.log(key)
                        return {
                            data: key,
                            title: key,
                            render: function (data, type, row, meta) {
                                if (detailUrl.endsWith('/')) {
                                    return `<a href="${detailUrl}${data}">${data}</a>`;
                                } else {
                                    return `<a href="${detailUrl}/${data}">${data}</a>`;
                                }
                            }
                        }
                    } else {
                        return { data: key, title: key, visible: false };
                    }
                }
                return { data: key, title: key };
            });
        }

        // Create the table with the data and column names
        let table = $(tableId).DataTable({
            data: data,
            columns: columns,
            initComplete: function () {
                setupColumnFilters(this);
            },
            order: [[1, 'asc']],
            paging: true,
            info: false,
            searching: true,
            scrollY: '50vh',
            scrollCollapse: true,
            scrollX: true
        });
 }

 function setUsersTable(tableId, detailUrl = null) {
    console.log('user_detail_url:' + detailUrl)
    $.ajax({
        url: "/hr_tool/all_users/",
        type: "GET",
        dataType: "json",
    }).done(function (data, textStatus, jqXHR) {
        createTable(data, tableId, detailUrl);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        console.log(textStatus);
        console.log(errorThrown);
    });
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





