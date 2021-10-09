run_migration() {
	cd /www/app
	alembic upgrade head
}

run_taskmanager_application() {
	python3 /www/app/main.py
}

run_migration
run_taskmanager_application
