<?php
// +----------------------------------------------------------------------
// | Description: 基础框架路由配置文件
// +----------------------------------------------------------------------
// | Author: 乌索普 <839804865@qq.com>
// +----------------------------------------------------------------------

return [
	// MISS路由
	'__miss__' => 'admin/base/miss',

	// 定义资源路由
	'__rest__' => [
		'admin/upload' => 'admin/upload',
		'admin/rules' => 'admin/rules',
		'admin/parameters' => 'admin/parameters',
		'admin/groups' => 'admin/groups',
		'admin/users' => 'admin/users',
		'admin/menus' => 'admin/menus',
		'admin/studios' => 'admin/studios',
		'admin/taches' => 'admin/taches',
		'admin/tachefileextensions' => 'admin/TacheFileExtensions',
		'admin/projects' => 'admin/projects',
		'admin/shots' => 'admin/shots',
		'admin/workbenches' => 'admin/workbenches',
		'admin/assets' => 'admin/assets',
		'admin/references' => 'admin/references',
		'admin/materials' => 'admin/materials',
		'admin/helps' => 'admin/helps',
		'admin/approvals' => 'admin/approvals',
		'admin/companies' => 'admin/companies',
		'admin/distributes' => 'admin/distributes',
		'admin/timelines' => 'admin/timelines',
		'admin/volumeStatistics' => 'admin/volumeStatistics',
		'admin/departments' => 'admin/departments',
		'admin/userSalaries' => 'admin/userSalaries',
		'admin/costStatistics' => 'admin/costStatistics',
		'admin/dailyStatistics' => 'admin/dailyStatistics',
		'admin/tasksMargin' => 'admin/tasksMargin',
		'admin/logstimes' => 'admin/logstimes',
		'admin/vendorapprovals' => 'admin/vendorApprovals',
		'admin/workplans' => 'admin/workPlans',
		'admin/workinfos' => 'admin/workinfos',
		'admin/exportHistories' => 'admin/exportHistories', //导出列表 删除
		'admin/planCycles' => 'admin/planCycles', //计划周期
	],


	// 项目统计
	'admin/volumeStatistics/task_status_num' => ['admin/volumeStatistics/task_status_num', ['method' => 'GET|POST']],
	'admin/volumeStatistics/task_status_user' => ['admin/volumeStatistics/task_status_user', ['method' => 'GET|POST']],
	// 测试 无验证权限
	'admin/test' => ['admin/tests/get_test', ['method' => 'GET|POST']],
	'admin/notice_test' => ['admin/tests/notice_test', ['method' => 'GET|POST']],
	'admin/swoole_test' => ['admin/tests/swoole_notice', ['method' => 'GET|POST']],
	'admin/set_data' => ['admin/tests/set_data', ['method' => 'GET|POST']],


	/**
	 * swoole异步队列curl推送消息
	 * @author 乌索普 2019/05/10
	 */
	'admin/swoole_notice' => ['admin/SwooleNotices/swoole_push', ['method' => 'POST']],
	'admin/swoole_timer' => ['admin/SwooleNotices/swoole_timer', ['method' => 'POST']],

	/**
	 * 忽略token 对外API
	 * @author 乌索普 2019/05/10
	 */
	# 批量修改新消息推送数据表主键从1开始
	'api/update_keys' => ['admin/ExecApi/update_primary_keys', ['method' => 'GET']],


	/**
	 * python 回调
	 * @author 乌索普 2018/06/15
	 */
	# python dailies 回调更新数据
	'callback/dailies' => ['admin/execpythons/update_task_byDailies', ['method' => 'POST|GET']],
	# python 上传单帧 回调更新数据
	'callback/frame_file' => ['admin/execpythons/frameFile', ['method' => 'POST|GET']],
	# python 参考库 回调更新数据
	'callback/reference' => ['admin/execpythons/update_byReferences', ['method' => 'POST|GET']],
	# python 获取未执行的脚本
	'python/getNonExecScript' => ['admin/execpythons/getPythonScript', ['method' => 'POST|GET']],
	# python 更新脚本状态
	'python/renewScriptStatus' => ['admin/execpythons/updatePythonStatus', ['method' => 'POST|GET']],
	# 批量新增生成的外包压缩包文件
	'python/add_download_link' => ['admin/execpythons/insert_download_link', ['method' => 'POST|GET']],
	#	python上传云的回调地址
	'python/distribute/callback' => ['admin/Execpythons/distribute_update_status', ['method' => 'POST|GET']],
	#	更新python收到消息的状态
	'python/update_exec_status' => ['admin/Execpythons/update_exec_status', ['method' => 'POST|GET']],
	# 前端检查所属任务ID及所属状态是否匹配
	'web/check_task_status' => ['admin/Execpythons/check_task_status', ['method' => 'GET']],
	# 是否打包成功
	'python/callback_pack_status' => ['admin/Execpythons/callback_pack_status', ['method' => 'GET']],
	# 下载完成回调
	'python/download_complete' => ['admin/Execpythons/callback_download_complete', ['method' => 'GET']],
	# 发送完成回调
	'python/send_complete' => ['admin/Execpythons/callback_send_complete', ['method' => 'GET']],
	# 剪辑线打包回调
	'python/clip_pack' => ['admin/Execpythons/callback_clip_pack', ['method' => 'GET']],
	# 镜头转制回调
	'python/shot_format' => ['admin/Execpythons/callback_shot_format', ['method' => 'GET']],
	# python 下载成功后通知制片
	'python/callback_distribute_download' => ['admin/Execpythons/distribute_download_callback', ['method' => 'GET']],
	# python 替换完图片通知
	'python/img_replace_callback' => ['admin/Execpythons/image_replace_callback', ['method' => 'GET']],
	# 获取上传外包dailies目录检查状态（true | false）
	'callback/checkVendorDailies' => ['admin/execpythons/check_vendorDailies_callback', ['method' => 'GET|POST']],
	# 获取外包dailies目录上传状态（true | false）
	'callback/upVendorDailies' => ['admin/execpythons/upload_vendorDailies_status', ['method' => 'GET|POST']],
	# 提交发布回调
	'callback/finishPublish' => ['admin/execpythons/finish_publish', ['method' => 'GET|POST']],

	/**
	 * 系统
	 * @author 乌索普 2018/01/22
	 */
	# 获取信息
	'admin/infos/index' => ['admin/infos/index', ['method' => 'POST']],
	# 刷新token
	'admin/infos/refresh' => ['admin/infos/refresh', ['method' => 'POST']],
	# 登录
	'admin/base/login' => ['admin/base/login', ['method' => 'POST|GET']],
	# 记住登录
	'admin/base/relogin' => ['admin/base/relogin', ['method' => 'POST']],
	# 修改密码
	'admin/base/setInfo' => ['admin/base/setInfo', ['method' => 'POST']],
	# 退出登录
	'admin/base/logout' => ['admin/base/logout', ['method' => 'POST']],
	# 获取配置
	'admin/base/getConfigs' => ['admin/base/getConfigs', ['method' => 'POST']],
	# 保存系统配置
	'admin/systemConfigs' => ['admin/systemConfigs/save', ['method' => 'POST']],
	# 获取验证码
	'admin/base/getVerify' => ['admin/base/getVerify', ['method' => 'GET']],


	/**
	 * 通用
	 * @author 乌索普 2018/07/13
	 */
	# 上传图片
	'admin/upload' => ['admin/upload/index', ['method' => 'POST']],
	# 上传缩略图
	'admin/upload_image' => ['admin/upload/images_add', ['method' => 'POST']],
	#获取分类下的子类型
	'admin/get_children' => ['admin/parameters/get_children_data', ['method' => 'GET']],
	# 根据所属用户获取镜头分配环节的模板
	'template/get_template' => ['admin/templates/get_template', ['method' => 'GET']],
	# 渲染是否启动
	'template/is_enable' => ['admin/parameters/render_is_enable', ['method' => 'GET']],
	# 设置启用 | 禁用
	'parameters/set_status' => ['admin/parameters/set_status', ['method' => 'GET|POST']],
	# 批量删除
	'parameters/deletes' => ['admin/parameters/deletes', ['method' => 'POST']],

	/**
	 * 规则
	 * @author 乌索普 2018/07/13
	 */
	# 批量删除
	'admin/rules/deletes' => ['admin/rules/deletes', ['method' => 'POST']],
	#	批量启用/禁用
	'admin/rules/enables' => ['admin/rules/enables', ['method' => 'POST']],


	/**
	 * 菜单
	 * @author 乌索普 2018/07/13
	 */
	#	批量删除
	'admin/menus/deletes' => ['admin/menus/deletes', ['method' => 'POST']],
	#	批量启用/禁用
	'admin/menus/enables' => ['admin/menus/enables', ['method' => 'POST']],



	/**
	 * 公司管理
	 * @author 2018/07/05
	 */
	#	批量删除
	'company/deletes' => ['admin/companies/deletes', ['method' => 'POST']],
	#	批量启用/禁用
	'company/enables' => ['admin/companies/enables', ['method' => 'POST']],
	# 获取外包公司
	'company/outsource_company' => ['admin/companies/get_outsource_company', ['method' => 'GET']],
	#	检测公司文件名是否冲突
	'company/checkCompanyDir' => ['admin/distributes/checkCompanyDir', ['method' => 'POST']],


	/**
	 * 工作室管理
	 * @author 乌索普 2018/03/22
	 */
	#	检查同属公司下是否有相同的工作室名称
	'admin/studios/check_name' => ['admin/studios/check_studio_name', ['method' => 'GET']],
	#	批量删除
	'admin/studios/deletes' => ['admin/studios/deletes', ['method' => 'POST']],
	#	批量启用/禁用
	'admin/studios/enables' => ['admin/studios/enables', ['method' => 'POST']],


	/**
	 * 环节管理
	 * @author 乌索普 2018/03/22
	 */
	#	批量删除
	'admin/taches/deletes' => ['admin/taches/deletes', ['method' => 'POST']],
	#	根据所属项目 及 环节显示出所属项目设定好的工作室
	'tache/get_studio' => ['admin/taches/studio_by_user', ['method' => 'GET|POST']],
	#	检查环节名称是否重复
	'tache/check_name' => ['admin/taches/check_tache_name', ['method' => 'GET']],
	# 根据不同类型(1镜头 2资产)获取环节列表
	'tache/get_tache' => ['admin/taches/tache_list', ['method' => 'GET']],
	# 编辑所属环节的扩展名称
	'tache/update_extension_name' => ['admin/TacheFileExtensions/update_extension_name', ['method' => 'POST']],
	# 根据所属环节新增扩展名
	'tache/addExtension_ByTache' => ['admin/TacheFileExtensions/addExtension_ByTache', ['method' => 'POST']],
	# 根据用户获取所属的环节下拉列表
	'tache/select_list' => ['admin/taches/select_list', ['method' => 'GET']],
	# 获取转制环节
	'tache/appoint_tache' => ['admin/taches/appoint_taches', ['method' => 'GET']],
	# 参考库中为选择的环节
	'tache/unselected_tache' => ['admin/taches/unselected_tache', ['method' => 'GET|POST']],

	/**
	 * 角色管理
	 * author 乌索普 2018/03/22
	 */
	#	批量删除
	'admin/groups/deletes' => ['admin/groups/deletes', ['method' => 'POST']],
	#	批量启用/禁用
	'admin/groups/enables' => ['admin/groups/enables', ['method' => 'POST']],


	/**
	 * 成员管理
	 * @author 乌索普 2018/03/22
	 */
	#	批量删除
	'admin/users/deletes' => ['admin/users/deletes', ['method' => 'POST']],
	#	批量启用/禁用
	'admin/users/enables' => ['admin/users/enables', ['method' => 'POST']],
	#	校验用名户重复
	'users/check_name' => ['admin/users/check_user_name', ['method' => 'GET']],
	#	根据外包管理员角色所属的用户获取去重后的公司
	'users/get_company' => ['admin/users/getCompany_ByUser', ['method' => 'GET']],
	# 根据所属角色获取用户
	'users/getuser_bygroup' => ['admin/users/getUser_ByGroup', ['method' => 'GET']],
	# 根据用户获取所属的环节下拉列表
	'users/select_list' => ['admin/users/select_list', ['method' => 'GET']],
	# 用户离职按钮
	'users/user_quit' => ['admin/users/quitById', ['method' => 'GET|POST']],
	# 人员统计编辑接口
	'users/statistics_user_update' => ['admin/users/statistics_user_update', ['method' => 'GET|POST']],


	/**
	 * 项目管理
	 * @author 乌索普 2018/04/22
	 */
	# 根据用户获取项目下拉列表
	'project/select_list' => ['admin/projects/select_list', ['method' => 'GET']],
	# 获取登陆者是否属于当前项目 应用于编辑操作的权限
	'admin/check_auth' => ['admin/projects/editProject_ByAuth', ['method' => 'POST']],
	# 校验项目简称是否重复
	'project/check_byname' => ['admin/projects/check_project_byname', ['method' => 'GET']],
	# 设置对项目设置暂停恢复
	'project/setup_is_pause' => ['admin/projects/setup_is_pause', ['method' => 'GET|POST']],
	# 根据项目获取包含的环节
	'project/getTache_ByProject' => ['admin/projects/getTache_ByProject', ['method' => 'GET']],
	# 获取项目的开始时间与结束时间
	'project/getProjectTime' => ['admin/projects/getProjectTime', ['method' => 'GET']],
	# 展示二级公司
	'project/getSecondCompany' => ['admin/projects/getSecondCompany', ['method' => 'GET']],
	# 根据所属项目绑定的二级公司进行展示
	'project/getLinkSecondCompany' => ['admin/projects/getSecondCompany', ['method' => 'GET']],
	# 获取工作计划
	'project/getWorkPlan' => ['admin/projects/getWorkPlan', ['method' => 'GET|POST']],
	# 修改项目是否为测试项目
	'project/update_is_test' => ['admin/projects/update_is_test', ['method' => 'GET|POST']],
	# 项目完成按钮操作
	'project/status_success' => ['admin/projects/status_success', ['method' => 'GET|POST']],
	# 项目下的镜头或资产统计
	'project/statistic' => ['admin/projects/statistic', ['method' => 'GET|POST']],
	# 修改计划结束时间
	'project/update_plan_end_time' => ['admin/projects/update_plan_end_time', ['method' => 'GET|POST']],
	# 项目详细信息
	'project/project_info' => ['admin/projects/project_info', ['method' => 'GET|POST']],
	# 项目工作量统计
	'project/work_statistics' => ['admin/projects/work_statistics', ['method' => 'GET|POST']],
	# 项目工作量统计导出表格
	'project/work_statistics_excel' => ['admin/projects/work_statistics_excel', ['method' => 'GET|POST']],
	# 获取项目颜色
	'project/get_project_color' => ['admin/projects/get_project_color', ['method' => 'GET|POST']],
	# 更改项目颜色
	'project/update_color' => ['admin/projects/update_color', ['method' => 'GET|POST']],
	# 工作量统计下钻镜头资产
	'project/work_statistics_resource_rih' => ['admin/projects/work_statistics_resource_rih', ['method' => 'GET|POST']],


	/**
	 * 今日计划 | 今日完成
	 */
	'work_plan/getDayPlan' => ['admin/workPlans/getDayPlan', ['method' => 'GET|POST']],


	/**
	 * 场/集管理
	 * @author 乌索普 2018/04/22
	 */
	#	添加场号
	'admin/save_field' => ['admin/fields/save_field', ['method' => 'POST']],
	#	获取场/集/资产类型列表
	'admin/get_fields' => ['admin/fields/get_field', ['method' => 'GET']],


	/**
	 * 剪辑线管理
	 * @author 弗兰奇 2018/07/02
	 */
	# 上传xml文件
	'admin/upload_xml' => ['admin/upload/upload_xml', ['method' => 'POST']],
	# 获取解析进度百分比
	'clips/get_progress' => ['admin/Clips/get_progress', ['method' => 'GET']],
	# 查看 python 是否完成写入
	'clips/check_python' => ['admin/Clips/check_py', ['method' => 'GET']],
	# 设置解析进度
	'clips/set_progress' => ['admin/upload/set_progress', ['method' => 'POST']],
	# 获取历史上传的列表
	'clips/get_history' => ['admin/Clips/get_history', ['method' => 'GET']],
	# 获取剪辑列表
	'clips/list' => ['admin/Clips/list', ['method' => 'GET']],
	# 上传批注图
	'clips/postil' => ['admin/Upload/upload_postil', ['method' => 'POST|GET']],
	# 批量分配
	'clips/allot' => ['admin/Clips/allot', ['method' => 'POST']],
	# 镜头添加分类
	'clips/add_classify' => ['admin/Clips/add_classify', ['method' => 'POST']],
	# 分类列表
	'clips/classify_list' => ['admin/Clips/classify_list', ['method' => 'GET']],
	# 单个分类下的所有镜头
	'clips/classify_shot' => ['admin/Clips/classify_shot', ['method' => 'POST']],
	# 关联资产或参考
	'clips/assets' => ['admin/Clips/relation_assets', ['method' => 'POST']],
	# 镜头下的所有反馈信息
	'clips/feedback_list' => ['admin/Clips/feedback_list', ['method' => 'GET']],
	# 所有的版本的信息，选择对比
	'clips/version_all' => ['admin/Clips/version_all', ['method' => 'POST']],
	# 分屏对比的两个版本
	'clips/version_contrast' => ['admin/Clips/version_contrast', ['method' => 'POST']],
	# 发布回复
	'clips/add_reply' => ['admin/Clips/add_reply', ['method' => 'POST']],
	# 审核通过
	'clips/clipAdopt' => ['admin/Clips/clipAdopt', ['method' => 'POST']],
	# 打包
	'clips/pack' => ['admin/Clips/pack', ['method' => 'POST']],
	# 获取打包进度
	'clips/pack_callback' => ['admin/Clips/pack_callback', ['method' => 'GET']],
	# 镜头信息
	'clips/shot_info' => ['admin/Clips/shot_info', ['method' => 'GET']],
	# 镜头批量分发
	'clips/batch_add_shots' => ['admin/Clips/batch_distribute_task', ['method' => 'POST']],
	# 删除上传的xml
	'clips/del_xml_field' => ['admin/Clips/del_xml_field', ['method' => 'GET']],


	/**
	 * 日期标注管理
	 * @author 弗兰奇 2018/08/29
	 */
	# 添加日期标注
	'dates/add_record' => ['admin/dates/add_record', ['method' => 'POST']],
	# 获取日期标注
	'dates/get_record' => ['admin/dates/get_record', ['method' => 'GET']],
	# 删除日期标注
	'dates/del_record' => ['admin/dates/delete', ['method' => 'GET']],


	/**
	 * 镜头管理
	 * @author 乌索普 2018/04/22
	 */
	# 镜头标准列表
	'shot/index_list' => ['admin/shots/index_list', ['method' => 'GET']],
	# 关联资产
	'shot/get_fields' => ['admin/shots/get_field', ['method' => 'GET']],
	# [镜头]上传excel文件用于获取模板
	'admin/upload_excel' => ['admin/upload/excels_add', ['method' => 'POST']],
	# 获取镜头号
	'admin/get_shot_num' => ['admin/shots/get_number', ['method' => 'GET']],
	# 参考获取镜头号
	'admin/reference_shot_num' => ['admin/shots/reference_get_number', ['method' => 'GET']],
	# 校验镜头编号是否重复
	'shot/check_num' => ['admin/shots/check_shot_number', ['method' => 'GET']],
	# 删除环节
	'shot/tache_del' => ['admin/shots/delete_tache', ['method' => 'GET']],
	# 批量删除场或镜头
	'admin/shots/deletes' => ['admin/shots/deletes', ['method' => 'POST']],
	# 获取模版
	'shot/template' => ['admin/shots/template', ['method' => 'POST']],
	# 获取update模板
	'shot/update_template' => ['admin/shots/update_template', ['method' => 'POST']],
	# 上传excel文件用于导入数据表
	'shot/import_excel' => ['admin/upload/shot_import_excel', ['method' => 'GET|POST']],
	# 上传excel文件根据文件内容批量修改镜头信息
	'shot/import_excel_update' => ['admin/upload/shot_import_excel_update', ['method' => 'GET|POST']],
	# source 导入
	'shot/import_source_excel' => ['admin/upload/import_source_excel', ['method' => 'GET|POST']],
	# 根据所属用户添加镜头分配环节模板
	'shot/save_tache_template' => ['admin/templates/save_template', ['method' => 'POST']],
	# 关联资产 资产列表(根据镜头ID获取去除原资产的资产列表)
	'shot/relevance_assets_list' => ['admin/shots/relevance_assets_index', ['method' => 'GET']],
	# 关联资产修改镜头
	'shot/relevance_asset' => ['admin/shots/relevance_assets', ['method' => 'POST']],
	# 设置样板镜头
	'shot/setup_templet' => ['admin/shots/setup_templet', ['method' => 'GET']],
	# 对镜头设置暂停恢复
	'shot/setup_pause' => ['admin/shots/setup_pause', ['method' => 'GET']],
	# 镜头批量分配任务进行校验工作室或公司
	'shot/batch_check' => ['admin/shots/batch_check_task', ['method' => 'GET|POST']],
	# 批量分配按钮
	'shot/batch_distribute' => ['admin/shots/batch_distribute_task', ['method' => 'GET|POST']],
	# 根据多镜头获取关联的资产(去重)
	'shot/getAssets_ByShotIds' => ['admin/shots/getAssets_ByShotIds', ['method' => 'POST']],
	# 镜头批量转制 废弃
	'shot/conversion' => ['admin/shots/conversion', ['method' => 'POST']],
	# 返回原始命名
	'shot/revert_original_name' => ['admin/shots/revert_original_name', ['method' => 'GET|POST']],
	# 检查 cmp 环节
	'shot/check_cmp_tache' => ['admin/shots/check_cmp_tache', ['method' => 'GET|POST']],
	# 检测素材号
	'shot/check_material' => ['admin/shots/check_material', ['method' => 'GET|POST']],
	# 打开镜头素材
	'shot/open_material' => ['admin/shots/open_material', ['method' => 'GET|POST']],
	# 镜头图片列表
	'shot/img_list' => ['admin/shots/img_list', ['method' => 'GET|POST']],
	# 补充图片
	'shot/supply_img' => ['admin/shots/supply_img', ['method' => 'GET|POST']],
	# 获取Python补传状态
	'shot/get_replace_img_status' => ['admin/shots/get_replace_image_status', ['method' => 'GET|POST']],
	# 所有镜头交货
	'shot/delivery' => ['admin/shots/delivery', ['method' => 'GET|POST']],
	# 修改镜头内部计划时长
	'shot/update_order_time' => ['admin/shots/update_order_time', ['method' => 'POST']],
	# 场统计
	'shot/field_statistic' => ['admin/shots/field_statistic', ['method' => 'GET|POST']],
	# 镜头导出
	'shot/export' => ['admin/shots/export', ['method' => 'GET|POST']],
	# 获取制作内容
	'shot/make_demand' => ['admin/shots/get_make_content', ['method' => 'GET|POST']],
	# 获取镜头交货日期去重
	'shot/delivery_date' => ['admin/shots/delivery_date', ['method' => 'GET|POST']],


	/**
	 * 历史导出页面
	 */
	# 下载
	'exportHistories/down_file' => ['admin/exportHistories/down_file', ['method' => 'GET|POST']],


	/**
	 * 资产库管理
	 * @author 乌索普 2018/06/22
	 */
	# 获取资产中文名称
	'asset/get_asset_name' => ['admin/assets/get_asset_name', ['method' => 'GET']],
	# 参考获取资产名
	'asset/reference_asset_name' => ['admin/assets/reference_asset_name', ['method' => 'GET']],
	# 校验资产类型名称是否重复
	'asset/check_byname' => ['admin/assets/check_asset_byname', ['method' => 'GET']],
	# 获取工作室列表
	'asset/get_studio' => ['admin/assets/get_studio_list', ['method' => 'GET']],
	# 删除环节
	'asset/tache_del' => ['admin/assets/delete_tache', ['method' => 'GET']],
	# 标准列表
	'asset/index_list' => ['admin/assets/index_list', ['method' => 'GET']],
	# 资产设置暂停恢复
	'asset/setup_is_pause' => ['admin/assets/setup_is_pause', ['method' => 'GET|POST']],
	# 批量分配按钮
	'asset/batch_distribute' => ['admin/assets/batch_distribute_task', ['method' => 'GET|POST']],
	# 资产概括
	'asset/survey' => ['admin/assets/survey', ['method' => 'GET|POST']],
	# 资产导入
	'asset/excel_asset' => ['admin/upload/asset_import_excel', ['method' => 'GET|POST']],
	# 任务导入
	'asset/excel_task' => ['admin/upload/excel_add_task', ['method' => 'GET|POST']],
	# 获取模版
	'asset/template' => ['admin/assets/template', ['method' => 'POST']],
	# 修改资产内部计划时长
	'asset/update_order_time' => ['admin/assets/update_order_time', ['method' => 'POST']],
	# 补充图片
	'asset/supply_img' => ['admin/assets/supply_img', ['method' => 'GET|POST']],
	# 获取Python补传状态
	'asset/get_replace_img_status' => ['admin/assets/get_replace_image_status', ['method' => 'GET|POST']],

	/**
	 * 分发平台
	 * @author 弗兰奇 2018/07/05
	 */
	#	获取分发记录
	'distribute/get_list' => ['admin/Distributes/get_list', ['method' => 'GET']],
	#	根据分发id获取未被选中的参考文件
	'distribute/get_reference' => ['admin/Distributes/get_reference', ['method' => 'GET']],
	#	发送压缩包
	'distribute/send' => ['admin/Distributes/send', ['method' => 'POST']],
	# 删除
	'distribute/del_ids' => ['admin/Distributes/del_ids', ['method' => 'GET|POST']],
	#	获取发送云状态
	'distribute/get_send_status' => ['admin/Distributes/send_callback', ['method' => 'GET']],
	#	打开文件夹
	'distribute/open_folder' => ['admin/Distributes/open_folder', ['method' => 'GET']],
	#	分发平台打包
	'distribute/pack' => ['admin/Distributes/pack', ['method' => 'POST']],
	#	分发平台下载
	'distribute/download' => ['admin/Distributes/download', ['method' => 'GET']],
	# 获取打包状态
	'distribute/pack_status' => ['admin/Distributes/pack_status', ['method' => 'GET']],
	# 获取分发平台去掉重复的镜头id
	'distribute/unique_shot' => ['admin/Distributes/get_unique_shot', ['method' => 'GET']],


	/**
	 * 工作台管理
	 * @author 乌索普 2018/06/21
	 */
	# 标准列表
	'task/index_list' => ['admin/workbenches/index_list', ['method' => 'GET']],
	# 改变状态
	'task/begin_task' => ['admin/workbenches/begin_task', ['method' => 'POST']],
	# 暂停列表
	'task/pause_task' => ['admin/workbenches/pause_list', ['method' => 'GET']],
	# 未分配列表
	'task/unallocated_task' => ['admin/workbenches/unallocated_list', ['method' => 'GET']],
	# 获取制作人列表
	'task/get_user' => ['admin/workbenches/get_user_list', ['method' => 'GET']],
	# 提交dailies
	'task/submit_dailies' => ['admin/workbenches/upload_dailies', ['method' => 'POST']],
	# 根据任务主键打开大样儿目录
	'task/open_master_dir' => ['admin/workbenches/open_dir', ['method' => 'GET']],
	# 提交发布
	'task/submitPublish' => ['admin/workbenches/submit_publish_by_uid', ['method' => 'GET']],
	# 提交发布完成
	'task/publish_finish' => ['admin/workbenches/finish_publish', ['method' => 'GET']],
	# 批量分配按钮
	'task/batch_distribute' => ['admin/workbenches/batch_distribute_task', ['method' => 'GET|POST']],
	# 获取环节详情
	'task/get_tache_task' => ['admin/workbenches/get_tache_info', ['method' => 'GET']],
	# 校验镜头 | 资产 是否包含制作中及以上状态的所属环节的顶级任务
	'task/check_tache_task' => ['admin/workbenches/check_tache_task', ['method' => 'GET']],
	# 提交发布文件从云上下载到本地服务器中
	'task/download_publish' => ['admin/workbenches/download_publish', ['method' => 'GET']],
	# 工作台效验
	'task/batch_check_task' => ['admin/workbenches/batch_check_task', ['method' => 'POST']],
	# 任务暂停
	'task/task_pause' => ['admin/workbenches/task_pause', ['method' => 'GET']],
	# 任务详情中分配制作人
	'task/distribute_user' => ['admin/workbenches/detail_distribution', ['method' => 'GET|POST']],
	# 渲染文件接口
	'task/render' => ['admin/workbenches/task_render', ['method' => 'GET|POST']],
	# 打开文件夹
	'task/open_folder' => ['admin/workbenches/folder', ['method' => 'GET|POST']],
	# 开始测试
	'task/begin_test' => ['admin/workbenches/begin_test_tasking', ['method' => 'GET|POST']],
	# 获取逾期
	'task/overdue_task' => ['admin/workbenches/get_overdue_task', ['method' => 'GET|POST']],
	'task/overdue_task_num' => ['admin/workbenches/get_overdue_task_num', ['method' => 'GET|POST']],
	# 获取上游
	'task/upper_task' => ['admin/workbenches/get_upper_task', ['method' => 'GET|POST']],
	# 工作台列表等待上游
	'task/get_upper_tache_task' => ['admin/workbenches/get_upper_tache_task', ['method' => 'GET|POST']],
	# 镜头或资根据简称增加主任务
	'task/add_main_task' => ['admin/workbenches/add_main_task', ['method' => 'GET|POST']],
	# 隐藏标签任务
	'task/delete_label' => ['admin/workbenches/delete_label_task', ['method' => 'GET|POST']],
	# 上传excel文件用于导入任务数据表
	'task/import_excel' => ['admin/upload/task_import_excel', ['method' => 'GET|POST']],
	# 获取模版
	'task/template' => ['admin/workbenches/template', ['method' => 'POST']],
	# 选择版本上传单帧图片
	'task/upload_frame_img' => ['admin/workbenches/uploadFrameImg', ['method' => 'GET|POST']],
	# 获取状态数量
	'task/status_num' => ['admin/workbenches/get_status_num', ['method' => 'GET|POST']],
	# 交付下游完成按钮通知接口
	'task/deliver_downstream_notice' => ['admin/workbenches/deliver_downstream_notice', ['method' => 'GET|POST']],
	# 获取个人或组内的制作任务
	'task/personal_task' => ['admin/workbenches/personal_task', ['method' => 'GET|POST']],
	# 项目工作量统计中通过环节主任务下钻返回数据接口
	'task/work_statistics_tache_rih' => ['admin/workbenches/work_statistics_tache_rih', ['method' => 'GET|POST']],


	/**
	 * 消息通知
	 * @author 弗兰奇 2018/12/11
	 */
	# 催促上游
	'notice/upper_reaches' => ['admin/noticeRecords/upper_reaches', ['method' => 'GET']],
	#消息列表
	'notice/list' => ['admin/Notices/index', ['method' => 'POST']],
	# 读取信息成功
	'notice/read' => ['admin/Notices/readNotice', ['method' => 'GET']],
	# 未读消息数量
	'notice/unreadcount' => ['admin/Notices/unReadCount', ['method' => 'GET']],
	# 用户消息分类配置列表
	'notice/setup_list' => ['admin/Notices/getSetup', ['method' => 'GET']],
	# 用户消息分类设置
	'notice/setup' => ['admin/Notices/noticeSetup', ['method' => 'POST']],
# 用户消息分类设置
	'notice/checkunread' => ['admin/Notices/checkunread', ['method' => 'GET']],
	# 消息一键删除
	'notice/del_notices' => ['admin/Notices/delete_all', ['method' => 'GET']],
	# 消息一键已读
	'notice/read_notices' => ['admin/Notices/read_all', ['method' => 'GET']],


	/**
	 * 审批管理
	 * @author 乌索普 2018/06/12
	 */
	# 生成base64格式的图片并上传到目录中
	'admin/image_base64' => ['admin/upload/images_base64_add', ['method' => 'POST']],
	# 操作为反馈中状态
	'approval/feedback_success' => ['admin/approvals/feedback_adopt', ['method' => 'GET']],
	# 内部审核通过
	'approval/examine_success' => ['admin/approvals/examine_adopt', ['method' => 'GET']],
	# 客户审核通过
	'approval/customer_success' => ['admin/approvals/customer_adopt', ['method' => 'GET']],
	# 客户已反馈
	'approval/customer_feedback' => ['admin/approvals/customer_feedback', ['method' => 'GET']],
	# 客户待审核
	'approval/customer_stay_examine' => ['admin/approvals/customer_stay_examine', ['method' => 'GET']],
	# 打开dailies目录
	'approval/open_dailies_dir' => ['admin/approvals/open_dailies_dir', ['method' => 'GET']],
	# 根据所属任务获取所有提交的版本
	'approval/get_version_data' => ['admin/approvals/getVersion_byTask', ['method' => 'GET']],
	# 上传单帧获取所有的版本
	'approval/task_version_all' => ['admin/approvals/taskVersionAll', ['method' => 'GET|POST']],
	# 播放dailies
	'approval/play_dailies' => ['admin/approvals/play_dailies', ['method' => 'GET']],
	# 上传截图反馈
	'approval/feedback_img' => ['admin/upload/upload_feedback_img', ['method' => 'POST']],
	# 文字反馈
	'approval/feedback_content' => ['admin/approvals/feedback_content', ['method' => 'POST|GET']],
	# 删除反馈（包括图片，评论全删除）
	'approval/feedback_del' => ['admin/approvals/deleteById', ['method' => 'GET']],
	# 批量下载dailies
	'approval/dailies_download' => ['admin/approvals/dailies_download', ['method' => 'GET|POST']],
	# dailies 关闭状态
	'approval/close_dailies' => ['admin/approvals/close_dailies', ['method' => 'GET']],
	# dailies撤回
	'approval/recall' => ['admin/approvals/recall', ['method' => 'GET']],
	# 获取审批模板
	'approval/template' => ['admin/approvals/template', ['method' => 'POST']],
	# 批量修改审批状态
	'approval/batch_operate' => ['admin/approvals/batch_operate', ['method' => 'GET|POST']],
	# 获取个人的工作记录
	'approval/work_record' => ['admin/approvals/work_record', ['method' => 'GET|POST']],
  # 创建剪辑线
	'approval/create_clip' => ['admin/approvals/create_clip', ['method' => 'GET|POST']],


	/**
	 * 反馈信息
	 * author 乌索普 2018/06/05
	 */
	# 添加反馈回复信息
	'feedback/add_info' => ['admin/FeedbackInfos/save_info', ['method' => 'GET']],
	# 根据审批ID获取所有的反馈回复
	'feedback/info_list' => ['admin/FeedbackInfos/get_info', ['method' => 'GET']],
	# 删除回复
	'feedback/info_del' => ['admin/FeedbackInfos/del_info', ['method' => 'GET']],


	/**
	 * 库管理
	 * @author 乌索普 2018/06/20
	 */
	/* 参考库管理 */
	# 查看公共分类列表
	'reference/common_type' => ['admin/references/common_type_list', ['method' => 'POST']],
	'reference/get_status' => ['admin/references/get_status', ['method' => 'GET']],
	# 打开参考文件目录
	'reference/open_dir' => ['admin/references/open_dir', ['method' => 'GET']],
	# 参考库关联镜头资产
	'reference/relation' => ['admin/references/referencesRelation', ['method' => 'GET|POST']],
	# 增加参考环节
	'reference/tache' => ['admin/references/add_tache', ['method' => 'GET|POST']],
	# 镜头资产关联参考
	'reference/resource_relation' => ['admin/references/resourceRelation', ['method' => 'GET|POST']],


	/**
	 * 问题反馈
	 * @author 乌索普 2018/05/16
	 */
	# 问题回复
	'help/add_answer' => ['admin/helps/save_problem', ['method' => 'POST']],
	# 根据单词模糊匹配相应记录
	'help/new_ask_word' => ['admin/helps/new_ask_push', ['method' => 'GET|POST']],
	# 查看所属问题所有回复
	'help/answer_list' => ['admin/helps/answer_list', ['method' => 'GET']],
	# 删除回复
	'help/del_answer' => ['admin/helps/delete_answer', ['method' => 'GET']],
	# 批量启用/禁用
	'admin/helps/enables' => ['admin/helps/enables', ['method' => 'POST']],
	# 批量删除
	'admin/helps/deletes' => ['admin/helps/deletes_by_ids', ['method' => 'POST']],


	/**
	 * 时间线
	 * @author 乌索普 2019/02/14
	 */

	/**
	 * 新统计
	 * * @author 弗兰奇 2019/05/31日
	 * statistic
	 */
	'statistic/get_field' => ['admin/statistics/get_field_info', ['method' => 'GET|POST']],
	'statistic/get_project_char' => ['admin/statistics/get_project_char_task', ['method' => 'GET|POST']],
	'statistic/get_projects_char' => ['admin/statistics/get_projects_char_task', ['method' => 'GET|POST']],
	'statistic/get_user' => ['admin/statistics/get_user_info', ['method' => 'GET|POST']],
	'statistic/get_basic' => ['admin/statistics/get_basic_statistics', ['method' => 'GET|POST']],
	'statistic/set_time' => ['admin/statistics/set_time', ['method' => 'GET|POST']],
	'statistic/task_statistics' => ['admin/statistics/project_statistics', ['method' => 'GET|POST']],
	'tasks_margin/difficulty' => ['admin/tasksMargin/task_difficulty_margin', ['method' => 'GET|POST']],

	# 范围统计
	'statistic/dailyStatistics' => ['admin/statistics/dateStatistic', ['method' => 'GET|POST']],
	# 人员统计列表
	'statistic/userList' => ['admin/statistics/userList', ['method' => 'GET|POST']],
	# 个人|组内|视效总监
	'statistic/personal_statistics' => ['admin/statistics/personal_statistics', ['method' => 'GET|POST']],

	/**
	 * 项目分辨率
	 * @author 弗兰奇 2019/04/08
	 * resolution
	 */
	# 获取所有分辨率
	'resolution/get_list' => ['admin/resolutionRatios/get_list', ['method' => 'GET']],
	# 添加新的分辨率  参数 resolution
	'resolution/add' => ['admin/resolutionRatios/add_data', ['method' => 'POST']],
	# 删除分辨率  参数 id
	'resolution/del' => ['admin/resolutionRatios/del', ['method' => 'GET']],

	/**
	 * 环节扩展名管理
	 * @author 弗兰奇 2019/04/11
	 * tache_extension
	 */
	# 获取所有扩展名
	'tache_extension/get_list' => ['admin/tacheExtensionNames/get_list', ['method' => 'GET']],
	# 添加新扩展名  参数 name
	'tache_extension/add' => ['admin/tacheExtensionNames/add_data', ['method' => 'POST']],
	# 删除扩展名  参数 id
	'tache_extension/del' => ['admin/tacheExtensionNames/del', ['method' => 'GET']],

	/**
	 * 下载
	 */
	'download/download_financial_count' => ['admin/download/download_financial_count', ['method' => 'GET']],

	/**
	 * 素材库打开目录
	 */
	'materials/open_dir' => ['admin/materials/open_dir', ['method' => 'GET']],

	/**
	 * 外包公司审批dailies模块
	 */
	# 外包dailies批量选择目录后的检测
	'vendor/approvals/check_dir' => ['admin/vendorApprovals/check_upload', ['method' => 'GET|POST']],
	# 外包dailies选择目录上传
	'vendor/approvals/upload' => ['admin/vendorApprovals/upload_dailies', ['method' => 'GET|POST']],
  # 上传外包缓存
  'vendor/upload_publish' =>['admin/vendorApprovals/upload_vendor_publish',['method'=>'GET']],


	/**
	 * 导入导出审批信息
	 */
	# 导入
	'admin/excel_approvals' => ['admin/upload/feedback_import_excel', ['method' => 'GET|POST']],
	# 导出反馈excel表 带图片
	'admin/export_approvals' => ['admin/approvals/export_excel_approvals', ['method' => 'GET|POST']],


	/**
	 * 工作内容
	 */
	# 环节下的 节能或者擅长
	'work_info/tache_skill' => ['admin/workInfos/get_infos', ['method' => 'GET|POST']],


	/**
	 * 环节负责人
	 */
	# 根据环节获取组长
	'tacheCadre/getCadreList' => ['admin/tacheCadres/getCadreList', ['method' => 'GET']],
	# 修改环节负责人
	'tacheCadre/update_user' => ['admin/tacheCadres/update_user', ['method' => 'GET|POST']],


	/**
	 * 任务计划周期
	 */
	# 添加任务计划周期
	'planCycles/add_time_cycle' => ['admin/planCycles/time_cycle', ['method' => 'GET|POST']],
	'planCycles/delete_cycle' => ['admin/planCycles/delete_id', ['method' => 'GET|POST']],
	'planCycles/update_cycle' => ['admin/planCycles/update_id', ['method' => 'GET|POST']],
	# 查当月计划周期
	'planCycles/user_time_cycle' => ['admin/planCycles/get_user_time_cycle', ['method' => 'GET|POST']],
	'planCycles/user_time_cycle1' => ['admin/planCycles/get_user_time_cycle1', ['method' => 'GET|POST']],
];

