class JSONFixture:

    @staticmethod
    def for_create_issue():
        json = {
            "fields": {
                "project":
                    {
                        "key": "AQAPYTHON"
                    },
                "summary": "Test Summary",
                "description": "Creating of an issue",
                "assignee": {"name": "webinar5"},
                "priority": {"name": "High"},
                "issuetype": {"name": "Bug"}
            }
        }
        return json
