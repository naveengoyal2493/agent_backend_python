from db.transactions.constants import SQLConstants as sc

class SQLStatements:


    @staticmethod
    def get_fmtsql_stmt(sql_stmt, replace_list):
        formatted_list = []
        for value in replace_list:
            if not value:
                formatted_list.append("null")
            else:
                formatted_list.append(f"'{value}'")
        return sql_stmt.format(rv=formatted_list)


    @staticmethod
    def update_user(update_value):
        return f"Update {sc.USER_TABLE} SET " + update_value + "={rv[1]} where " + sc.USER_ID + " = {rv[0]}"


    INSERT_USER = f"INSERT INTO {sc.USER_TABLE} ({sc.USER_ID}, {sc.USER_NAME}, {sc.USER_DOB}, {sc.USER_GENDER}, \
                                {sc.USER_EMAIL})" + " VALUES ({rv[0]}, {rv[1]}, STR_TO_DATE({rv[2]}, '%d-%m-%Y'), {rv[3]}, {rv[4]})"
        
    DELETE_USER = f"DELETE FROM {sc.USER_TABLE} where {sc.USER_ID} = " + "{rv[0]}"
    
    SELECT_USER = f"SELECT {sc.USER_NAME}, {sc.USER_EMAIL}, {sc.USER_DOB}, {sc.USER_GENDER} from {sc.USER_TABLE} where {sc.USER_ID} = " + "{rv[0]}"

    INSERT_POLICY = f"INSERT INTO {sc.USER_TABLE} ({sc.USER_ID}, {sc.USER_NAME}, {sc.USER_DOB}, {sc.USER_GENDER}, \
                                {sc.USER_EMAIL})" + " VALUES ({rv[0]}, {rv[1]}, STR_TO_DATE({rv[2]}, '%d-%m-%Y'), {rv[3]}, {rv[4]})"